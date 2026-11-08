#!/usr/bin/env python3
"""Run: python3 test_render_inventory.py from this directory, or pass this file to python3."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import render_inventory as renderer


def sample_inventory() -> renderer.Inventory:
    project = renderer.Project(
        name='Rules <script>',
        path="/Users/example/Development/rules",
        summary="",
        repos=(
            renderer.Repo("https://github.com/example/rules", "origin"),
            renderer.Repo("https://gitlab.com/example/rules", "mirror"),
        ),
        server_resources=(
            renderer.ServerResource("Fly.io", "app", "rules", "iad", "fly.toml"),
        ),
        stack=("Python",),
        default_branch="",
        last_commit="2026-11-01",
        notes="Paused until the glossary lands.",
        unknowns=("No region in the worker config.",),
    )
    other = renderer.Project(
        name="Notes",
        path="",
        summary="A folder of notes.",
        repos=(renderer.Repo("git@gitlab.com:example/notes.git", "origin"),),
        server_resources=(),
        stack=(),
        default_branch="main",
        last_commit="",
        notes="",
        unknowns=(),
    )
    return renderer.Inventory("2026-11-07", "/Users/example/Development", (project, other))


class RenderInventoryTest(unittest.TestCase):
    def test_report_includes_evidence_and_escapes_text(self):
        html = renderer.render_html(sample_inventory())

        self.assertIn("Project Inventory", html)
        self.assertIn("2026-11-07", html)
        self.assertIn("/Users/example/Development", html)
        self.assertNotIn("<script>", html)
        self.assertIn("Rules &lt;script&gt;", html)
        self.assertIn("https://github.com/example/rules", html)
        self.assertIn("Fly.io", html)
        self.assertIn("fly.toml", html)
        self.assertIn("No summary recorded.", html)
        self.assertIn("Not recorded", html)
        self.assertIn("Paused until the glossary lands.", html)
        self.assertIn("No region in the worker config.", html)
        self.assertIn("No server resources recorded.", html)
        self.assertIn("No GitHub repo recorded.", html)
        self.assertIn('class="n">2</span><span class="l">Projects', html)
        self.assertIn('class="n">1</span><span class="l">GitHub repos', html)
        self.assertIn('class="n">1</span><span class="l">Server resources', html)
        self.assertIn('class="n">1</span><span class="l">Providers', html)

    def test_empty_inventory_states_that_no_projects_are_recorded(self):
        html = renderer.render_html(renderer.Inventory("2026-11-07", "/Users/example/Development", ()))

        self.assertIn("No projects in this inventory yet.", html)
        self.assertIn('class="n">0</span><span class="l">Projects', html)

    def test_load_record_rejects_a_project_without_a_name(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "projects.json"
            path.write_text(
                json.dumps({"updated": "2026-11-07", "development_root": "/tmp", "projects": [{}]}),
                encoding="utf-8",
            )
            with self.assertRaises(renderer.InventoryError) as raised:
                renderer.load_record(path)

        self.assertIn("name", str(raised.exception))

    def test_host_is_the_url_host_not_a_substring(self):
        self.assertFalse(renderer.is_github("https://example.com/github.com/repo"))
        self.assertEqual(renderer.host_label("git@github.com:example/rules.git"), "GitHub")
        self.assertEqual(renderer.host_label("https://gitlab.com/example/rules"), "GitLab")

    def test_load_record_reads_a_valid_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "projects.json"
            path.write_text(
                json.dumps(
                    {
                        "updated": "2026-11-07",
                        "development_root": "/Users/example/Development",
                        "projects": [
                            {
                                "name": "rules",
                                "repos": [{"url": "https://github.com/example/rules"}],
                                "server_resources": [{"provider": "Fly.io", "resource_type": "app"}],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            inventory = renderer.load_record(path)

        self.assertEqual(inventory.projects[0].name, "rules")
        self.assertEqual(inventory.projects[0].repos[0].remote, "")
        self.assertEqual(inventory.projects[0].server_resources[0].region, "")


if __name__ == "__main__":
    unittest.main()
