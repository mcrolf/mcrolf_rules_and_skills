---
name: project-inventory
description: >-
  Builds and updates a personal inventory of development projects as HTML and
  a PDF rendered from that HTML, in ~/Development/Project_Inventory. Records
  project name, GitHub repos, server resources (provider, resource type, and
  related facts), and other evidenced notes a developer needs to track those
  projects. Use when the user asks for project-inventory, a project inventory,
  an inventory report of their Development folder, or to track GitHub repos
  and server resources across local projects. If no projects are specified,
  ask which Development projects to include. If the report already exists,
  ask whether to include new projects or update an existing project.
---

# Project Inventory

Keep one inventory report for the projects in the user's Development folder. The report is HTML, plus a PDF rendered from that HTML.

## Where it lives

Use `~/Development/Project_Inventory/`. Create that folder when it is missing. Do not create `~/Development` itself. If that folder is missing, ask where the Development folder is and wait.

Stable files, so a later run finds the same report:

- `projects.json`: the inventory record. The HTML is rendered from it, so one project can change without dropping the others.
- `inventory.html`
- `inventory.pdf`

If `inventory.html` exists and `projects.json` does not, stop and ask before replacing the HTML.

## Ask

Read the user's message first. Ask only for a choice they have not already made, then wait.

No report yet, and no projects specified: list the candidate projects in the Development folder and ask which of those projects they want in the inventory report.

The report already exists, and they did not already say what to change: ask if they would like to include new projects or update an existing project inside the report.

- Include new projects: list Development projects that are not already in the report, ask which to add, wait, then append those entries.
- Update an existing project: list the projects already in the report, ask which to update, wait, then refresh only those entries.

A named project that is already in the report is an update, not a second copy. Leave every unselected project as it is, including its notes.

## Candidates

A candidate is a directory directly inside the Development folder with a `.git` directory or a project manifest (`package.json`, `pyproject.toml`, `setup.py`, `Cargo.toml`, `go.mod`, `Gemfile`, `pom.xml`, `build.gradle`, `build.gradle.kts`, `composer.json`, `Package.swift`, `mix.exs`, `pubspec.yaml`, or a `.sln` file). Skip `Project_Inventory`, hidden directories, and files.

Show each candidate as its directory name and its GitHub remote, or "no GitHub remote". Do not inspect server resources until they choose. If they name a folder that was not listed, use that folder and say what was missing.

## What to record

Evidence only, from the selected repo or from the user. Do not invent a provider, region, repo, or stack. Do not log into a cloud account or call a provider API. Do not copy secrets, `.env` values, tokens, keys, or connection strings.

| Field | What to write |
| --- | --- |
| name | Directory name, unless the README title or the user gives a clearer project name |
| path | Absolute path |
| summary | One sentence from the README or the user |
| repos | Every git remote (`url`, `remote` name), written as `https://github.com/owner/repo` when the remote is GitHub. Also URLs in `.gitmodules`. If there is no remote, use a `github.com` URL from the README or a manifest `repository` field, with `remote` empty |
| server_resources | One object per resource the repo actually configures |
| stack | Languages and frameworks named by the root manifests |
| default_branch | Current HEAD branch name |
| last_commit | HEAD commit date, `YYYY-MM-DD` |
| notes | Only what the user asked to store. On update, keep existing notes unless they change them |
| unknowns | Useful facts you looked for and did not find |

A server resource has `provider`, `resource_type`, `name`, `region`, and `evidence`. Resource type is the kind of thing that runs or stores data: app, database, bucket, worker, function, static site, queue, or the type the file itself uses. Region and name may be empty when the file does not state them. `evidence` is the repo path that showed the resource.

Look for: `fly.toml`, `vercel.json`, `.vercel/project.json`, `render.yaml`, `railway.toml`, `railway.json`, `Dockerfile`, `docker-compose.yml`, `supabase/config.toml`, `convex.json`, `wrangler.toml`, `netlify.toml`, `app.yaml`, `serverless.yml`, `Procfile`, `app.json`, `amplify.yml`, `sst.config.*`, Terraform or Pulumi files, and deploy workflows in `.github/workflows`. A Dockerfile with no host is provider unknown and resource type container. Skip `node_modules`, lockfiles, and vendored dependencies.

Set `updated` to today's date (`YYYY-MM-DD`) and `development_root` to the absolute Development folder. Write `projects.json` as UTF-8 with two-space indent. On an update, replace that project in place. On an add, append.

```json
{
  "updated": "2026-11-07",
  "development_root": "/Users/example/Development",
  "projects": [
    {
      "name": "example",
      "path": "/Users/example/Development/example",
      "summary": "One sentence from the README.",
      "repos": [{ "url": "https://github.com/example/example", "remote": "origin" }],
      "server_resources": [
        {
          "provider": "Fly.io",
          "resource_type": "app",
          "name": "example",
          "region": "iad",
          "evidence": "fly.toml"
        }
      ],
      "stack": ["Go"],
      "default_branch": "main",
      "last_commit": "2026-11-01",
      "notes": "",
      "unknowns": []
    }
  ]
}
```

## Render

From this skill's directory (the folder that contains this file):

```bash
python3 scripts/render_inventory.py "$HOME/Development/Project_Inventory"
```

Pass the `Project_Inventory` directory you created when it is not under `~/Development`. The script writes `inventory.html`, then `inventory.pdf` from that HTML. If it cannot render the PDF, it leaves the HTML in place, keeps the previous PDF if there was one, and exits with a reason. Say that reason in chat. The HTML is then newer than the PDF.

Then give the absolute paths of the HTML and the PDF, which projects were added or updated, and any unknowns the user needs to fill.

Follow the no-em-dash rule in the report text and the chat summary. The renderer escapes record text; write facts, not HTML.
