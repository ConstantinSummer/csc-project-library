# CSC Naming and Versioning

These conventions apply to Computer Science Center (CSC) educational projects and the central catalogue. Maintainer: **Konstantinos Zitis**. Education website: [https://csc.gr](https://csc.gr).

## Repository names

Use `csc-<technology>-<project-name>` for application repositories.

- Use lowercase ASCII letters, digits and single hyphens between words.
- Choose a short, descriptive application name; avoid spaces, underscores and version numbers.
- Select one primary technology identifier even when an application uses several technologies.
- Keep `csc-project-library` as the name of the central catalogue and standards repository.

| Catalogue area | Technology identifier |
| --- | --- |
| Java | `java` |
| Python | `python` |
| Data Structures & Algorithms | `dsa` |
| Dart | `dart` |
| Flutter | `flutter` |
| Web | `web` |
| Databases | `databases` |
| AI | `ai` |

For example, `csc-java-task-manager` illustrates the naming format only; it is not an existing or committed project plan.

## Folder names

Use short, lowercase, hyphen-separated names for general documentation and resource folders, such as `docs`, `sample-data` and `design-notes`. Do not include spaces or release numbers in folder names.

Follow language and framework conventions for source packages and generated structures: for example, Python packages use `snake_case`, and Java packages use lowercase package segments. Do not rename tool-required folders to force the general rule.

The central library uses `docs/`, `catalog/` and `templates/`. Conventional documentation filenames such as `README.md` and the shared standard filenames retain their documented capitalization. Respect filename case in links across operating systems.

## Branch names

Keep `main` as the stable default branch. Use short-lived branches named `<type>/<short-description>` in lowercase, with hyphens between description words.

| Type | Purpose | Example |
| --- | --- | --- |
| `docs` | Documentation and catalogue updates | `docs/clarify-setup` |
| `feat` | New application behaviour | `feat/add-search` |
| `fix` | Bug fixes | `fix/handle-empty-input` |
| `refactor` | Internal restructuring without intended behaviour changes | `refactor/split-storage-layer` |
| `test` | Validation coverage | `test/add-storage-checks` |
| `chore` | Maintenance and tooling | `chore/update-dependencies` |

An issue number may follow the type, for example `fix/42-handle-empty-input`. Keep a branch focused on one coherent change and remove it after merging when no longer needed.

## Semantic Versioning and releases

Use versions in the form `MAJOR.MINOR.PATCH`, with Git tags prefixed by `v`, such as `v1.0.0`. Start the first complete, documented teaching baseline at `v1.0.0`; use `v0.x.y` for explicitly unfinished development snapshots if needed.

For CSC projects, compatibility includes documented interfaces, stored-data formats, supported execution environments and the setup or learner workflow used by lessons.

| Increment | When to use it | Example |
| --- | --- | --- |
| Major | Existing documented usage or lesson setup becomes incompatible, such as a breaking data format or required runtime change | `v1.4.2` → `v2.0.0` |
| Minor | Backward-compatible features or substantial new educational content, such as an optional extension challenge | `v1.4.2` → `v1.5.0` |
| Patch | Backward-compatible bug fixes, corrections or documentation clarifications | `v1.4.2` → `v1.4.3` |

Incrementing a major or minor version resets the lower components to zero. Optional prereleases use a suffix such as `v1.1.0-rc.1` and must be labelled as prereleases rather than stable teaching baselines.

Create a tag on the verified commit and publish release notes describing changes, setup impacts and any migration steps. Never move a published version tag to different content; publish a new version instead. Keep each release's documentation accurate for its code, and point the catalogue to an explicit stable release.

The catalogue may evolve through ordinary documentation commits without a release for every edit. If the central standards are released, use the same version format, treating incompatible mandatory-standard changes as major changes.

## Commit messages

Use `<type>: <imperative summary>`, optionally adding a scope: `<type>(<scope>): <imperative summary>`. Use the branch types listed above, keep the subject concise and omit a trailing full stop.

Examples:

```text
docs: Add Python catalogue entry
docs(standard): Clarify execution requirements
feat: Add task filtering
fix: Handle empty input
```

Use the body to explain why a non-obvious change is needed and describe compatibility impacts. Mark breaking changes with `!` after the type or scope and include a `BREAKING CHANGE:` explanation in the body. Keep each commit focused and never include credentials or unrelated generated artefacts.

Commit messages, tags and tag messages must not contain AI-tool attribution or session metadata; see **No AI Attribution Metadata** in the [CSC project standard](PROJECT_STANDARD.md).

For the initial library commit, use `Initialize CSC educational project library` as the explicit bootstrap-message exception.
