#!/usr/bin/env python3
"""Render the project inventory HTML, then a PDF from that HTML.

Check: python3 scripts/test_render_inventory.py from this directory.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from html import escape
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "templates" / "inventory.html"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MAC_BROWSERS = (
    "Google Chrome.app/Contents/MacOS/Google Chrome",
    "Chromium.app/Contents/MacOS/Chromium",
    "Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "Brave Browser.app/Contents/MacOS/Brave Browser",
)
PATH_BROWSERS = (
    "google-chrome",
    "chromium",
    "chromium-browser",
    "brave-browser",
    "microsoft-edge",
)


class InventoryError(Exception):
    """The inventory record or template cannot be rendered."""


class PdfError(Exception):
    """The HTML was written, and the PDF was not."""


@dataclass(frozen=True)
class Repo:
    url: str
    remote: str


@dataclass(frozen=True)
class ServerResource:
    provider: str
    resource_type: str
    name: str
    region: str
    evidence: str


@dataclass(frozen=True)
class Project:
    name: str
    path: str
    summary: str
    repos: tuple[Repo, ...]
    server_resources: tuple[ServerResource, ...]
    stack: tuple[str, ...]
    default_branch: str
    last_commit: str
    notes: str
    unknowns: tuple[str, ...]


@dataclass(frozen=True)
class Inventory:
    updated: str
    development_root: str
    projects: tuple[Project, ...]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: render_inventory.py <Project_Inventory directory>", file=sys.stderr)
        return 2
    directory = Path(argv[1])
    try:
        inventory = load_record(directory / "projects.json")
        html = render_html(inventory)
    except InventoryError as error:
        print(error, file=sys.stderr)
        return 2
    html_path = directory / "inventory.html"
    html_path.write_text(html, encoding="utf-8")
    try:
        write_pdf(html_path, directory / "inventory.pdf")
    except PdfError as error:
        print(error, file=sys.stderr)
        return 3
    print(html_path.resolve())
    print((directory / "inventory.pdf").resolve())
    return 0


def load_record(path: Path) -> Inventory:
    if not path.is_file():
        raise InventoryError(f"Inventory record is missing: {path}")
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise InventoryError(f"{path.name} is not valid JSON: {error}") from error
    if not isinstance(raw, dict):
        raise InventoryError(f"{path.name} must be a JSON object.")
    updated = required_text(raw, "updated", path.name)
    if DATE.fullmatch(updated) is None:
        raise InventoryError(f"{path.name} updated must be YYYY-MM-DD.")
    root = required_text(raw, "development_root", path.name)
    projects = raw.get("projects")
    if not isinstance(projects, list):
        raise InventoryError(f"{path.name} projects must be a list.")
    return Inventory(
        updated,
        root,
        tuple(load_project(item, index) for index, item in enumerate(projects, start=1)),
    )


def load_project(item: object, index: int) -> Project:
    label = f"projects[{index}]"
    if not isinstance(item, dict):
        raise InventoryError(f"{label} must be an object.")
    name = required_text(item, "name", label)
    label = f"projects[{index}] ({name})"
    return Project(
        name=name,
        path=optional_text(item, "path", label),
        summary=optional_text(item, "summary", label),
        repos=tuple(
            load_repo(entry, label, entry_index)
            for entry_index, entry in enumerate(list_of(item, "repos", label), start=1)
        ),
        server_resources=tuple(
            load_resource(entry, label, entry_index)
            for entry_index, entry in enumerate(list_of(item, "server_resources", label), start=1)
        ),
        stack=tuple(string_list(item, "stack", label)),
        default_branch=optional_text(item, "default_branch", label),
        last_commit=optional_date(item, "last_commit", label),
        notes=optional_text(item, "notes", label),
        unknowns=tuple(string_list(item, "unknowns", label)),
    )


def load_repo(item: object, label: str, index: int) -> Repo:
    where = f"{label} repos[{index}]"
    if not isinstance(item, dict):
        raise InventoryError(f"{where} must be an object.")
    return Repo(required_text(item, "url", where), optional_text(item, "remote", where))


def load_resource(item: object, label: str, index: int) -> ServerResource:
    where = f"{label} server_resources[{index}]"
    if not isinstance(item, dict):
        raise InventoryError(f"{where} must be an object.")
    return ServerResource(
        provider=required_text(item, "provider", where),
        resource_type=required_text(item, "resource_type", where),
        name=optional_text(item, "name", where),
        region=optional_text(item, "region", where),
        evidence=optional_text(item, "evidence", where),
    )


def required_text(item: dict, field: str, label: str) -> str:
    value = optional_text(item, field, label)
    if not value:
        raise InventoryError(f"{label} is missing {field}.")
    return value


def optional_text(item: dict, field: str, label: str) -> str:
    value = item.get(field, "")
    if value is None:
        return ""
    if not isinstance(value, str):
        raise InventoryError(f"{label} field {field} must be a string.")
    return value.strip()


def optional_date(item: dict, field: str, label: str) -> str:
    value = optional_text(item, field, label)
    if value and DATE.fullmatch(value) is None:
        raise InventoryError(f"{label} field {field} must be YYYY-MM-DD.")
    return value


def list_of(item: dict, field: str, label: str) -> list:
    value = item.get(field, [])
    if value is None:
        return []
    if not isinstance(value, list):
        raise InventoryError(f"{label} field {field} must be a list.")
    return value


def string_list(item: dict, field: str, label: str) -> list[str]:
    values = []
    for index, entry in enumerate(list_of(item, field, label), start=1):
        if not isinstance(entry, str):
            raise InventoryError(f"{label} field {field}[{index}] must be a string.")
        text = entry.strip()
        if text:
            values.append(text)
    return values


def render_html(inventory: Inventory) -> str:
    if not TEMPLATE.is_file():
        raise InventoryError(f"Inventory template is missing: {TEMPLATE}")
    html = TEMPLATE.read_text(encoding="utf-8")
    html = fill(html, "UPDATED", escape(inventory.updated))
    html = fill(html, "ROOT", f"<code>{escape(inventory.development_root)}</code>")
    html = fill(html, "SUMMARY", render_summary(inventory))
    html = fill(html, "PROJECTS", render_projects(inventory.projects))
    return html


def fill(template: str, marker: str, content: str) -> str:
    start = f"<!-- {marker} -->"
    end = f"<!-- /{marker} -->"
    if start not in template or end not in template:
        raise InventoryError(f"Template is missing the {marker} slot.")
    before, _, rest = template.partition(start)
    _, found, after = rest.partition(end)
    if not found:
        raise InventoryError(f"Template is missing the {marker} slot.")
    return f"{before}{start}\n{content}\n{end}{after}"


def render_summary(inventory: Inventory) -> str:
    github_repos = 0
    resource_count = 0
    providers: set[str] = set()
    for project in inventory.projects:
        github_repos += sum(1 for repo in project.repos if is_github(repo.url))
        resource_count += len(project.server_resources)
        providers.update(resource.provider.casefold() for resource in project.server_resources)
    stats = (
        (len(inventory.projects), "Projects"),
        (github_repos, "GitHub repos"),
        (resource_count, "Server resources"),
        (len(providers), "Providers"),
    )
    cells = [
        f'<div class="stat"><span class="n">{count}</span><span class="l">{escape(label)}</span></div>'
        for count, label in stats
    ]
    return '<div class="summary-grid">' + "".join(cells) + "</div>"


def render_projects(projects: tuple[Project, ...]) -> str:
    if not projects:
        return '<p class="missing">No projects in this inventory yet.</p>'
    return "\n".join(render_project(project, index) for index, project in enumerate(projects, start=1))


def render_project(project: Project, index: int) -> str:
    parts = [
        '<article class="project">',
        f'<div class="index">{index:02d}</div>',
        '<div class="body">',
        f"<h2>{escape(project.name)}</h2>",
        paragraph(project.summary, "No summary recorded.", "summary"),
        fields_html(project),
        "<h3>Repos</h3>",
        repos_html(project.repos),
        "<h3>Server resources</h3>",
        resources_html(project.server_resources),
    ]
    if project.notes:
        parts.extend(("<h3>Notes</h3>", f'<p class="notes">{escape(project.notes)}</p>'))
    if project.unknowns:
        items = "".join(f"<li>{escape(item)}</li>" for item in project.unknowns)
        parts.extend(("<h3>Unknowns</h3>", f'<ul class="unknowns">{items}</ul>'))
    parts.extend(("</div>", "</article>"))
    return "\n".join(parts)


def fields_html(project: Project) -> str:
    stack = ", ".join(project.stack)
    rows = (
        ("Path", code_or_missing(project.path)),
        ("Default branch", text_or_missing(project.default_branch)),
        ("Last commit", text_or_missing(project.last_commit)),
        ("Stack", text_or_missing(stack)),
    )
    body = "".join(f"<dt>{escape(label)}</dt><dd>{value}</dd>" for label, value in rows)
    return f'<dl class="fields">{body}</dl>'


def repos_html(repos: tuple[Repo, ...]) -> str:
    if not repos:
        return '<p class="missing">No GitHub repo recorded.</p>'
    items = []
    if not any(is_github(repo.url) for repo in repos):
        items.append('<li class="missing">No GitHub repo recorded.</li>')
    for repo in repos:
        remote = f' <span class="remote">{escape(repo.remote)}</span>' if repo.remote else ""
        items.append(
            f"<li><span class=\"host\">{escape(host_label(repo.url))}</span> {linkify(repo.url)}{remote}</li>"
        )
    return '<ul class="repos">' + "".join(items) + "</ul>"


def resources_html(resources: tuple[ServerResource, ...]) -> str:
    if not resources:
        return '<p class="missing">No server resources recorded.</p>'
    rows = []
    for resource in resources:
        cells = (
            escape(resource.provider),
            escape(resource.resource_type),
            text_or_missing(resource.name),
            text_or_missing(resource.region),
            code_or_missing(resource.evidence),
        )
        rows.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in cells) + "</tr>")
    header = (
        "<thead><tr><th>Provider</th><th>Resource type</th>"
        "<th>Name</th><th>Region</th><th>Evidence</th></tr></thead>"
    )
    return f'<table class="resources">{header}<tbody>{"".join(rows)}</tbody></table>'


def paragraph(value: str, empty: str, class_name: str) -> str:
    if not value:
        return f'<p class="{class_name} missing">{escape(empty)}</p>'
    return f'<p class="{class_name}">{escape(value)}</p>'


def text_or_missing(value: str) -> str:
    if not value:
        return '<span class="missing">Not recorded</span>'
    return escape(value)


def code_or_missing(value: str) -> str:
    if not value:
        return '<span class="missing">Not recorded</span>'
    return f"<code>{escape(value)}</code>"


def linkify(url: str) -> str:
    shown = escape(url)
    if url.startswith("https://") or url.startswith("http://"):
        return f'<a href="{shown}">{shown}</a>'
    return shown


def is_github(url: str) -> bool:
    host = repo_host(url)
    return host == "github.com" or host.endswith(".github.com")


def host_label(url: str) -> str:
    host = repo_host(url)
    if is_github(url):
        return "GitHub"
    if host == "gitlab.com":
        return "GitLab"
    if host == "bitbucket.org":
        return "Bitbucket"
    return "Other"


def repo_host(url: str) -> str:
    text = url.strip().lower()
    if "://" in text:
        host = text.split("://", 1)[1].split("/", 1)[0]
    elif text.startswith("git@"):
        host = text[4:].split(":", 1)[0]
    else:
        host = text.split("/", 1)[0]
    return host.split("@")[-1].split(":")[0]


def write_pdf(html_path: Path, pdf_path: Path) -> None:
    browser = find_browser()
    target = pdf_path.resolve()
    partial = target.with_suffix(".pdf.partial")
    # An absolute print path is required. A relative one is written from the browser cwd.
    url = html_path.resolve().as_uri()
    last_error = ""
    for headless in ("--headless=new", "--headless"):
        partial.unlink(missing_ok=True)
        command = [
            str(browser),
            headless,
            "--disable-gpu",
            "--no-first-run",
            "--no-pdf-header-footer",
            f"--print-to-pdf={partial}",
            url,
        ]
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=60)
        except subprocess.TimeoutExpired:
            last_error = f"{browser.name} timed out while rendering the PDF."
            continue
        if result.returncode == 0 and is_pdf(partial):
            partial.replace(target)
            return
        detail = (result.stderr or result.stdout or "").strip()
        if len(detail) > 500:
            detail = detail[-500:]
        last_error = detail or f"{browser.name} exited {result.returncode} without a PDF."
    partial.unlink(missing_ok=True)
    kept = " The previous PDF was left unchanged." if target.is_file() else ""
    raise PdfError(f"Could not render the PDF from {html_path.name} with {browser.name}. {last_error}{kept}")


def find_browser() -> Path:
    roots = (Path("/Applications"), Path.home() / "Applications")
    for root in roots:
        for relative in MAC_BROWSERS:
            candidate = root / relative
            if candidate.is_file():
                return candidate
    for name in PATH_BROWSERS:
        found = shutil.which(name)
        if found:
            return Path(found)
    raise PdfError("No Chrome, Chromium, Edge, or Brave browser was found to render the PDF from the HTML.")


def is_pdf(path: Path) -> bool:
    if not path.is_file() or path.stat().st_size < 5:
        return False
    return path.read_bytes()[:5] == b"%PDF-"


if __name__ == "__main__":
    sys.exit(main(sys.argv))
