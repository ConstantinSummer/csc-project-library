#!/usr/bin/env python3
"""Create the boilerplate of a new CSC educational project repository.

The scaffolder copies and fills the existing CSC templates; it does not define
any standard of its own. It only writes files into a NEW directory: it refuses
to touch an existing path, never creates screenshots, releases or tags, never
initialises git and never pushes.

Example (from the csc-project-library folder):

    python tools/new-project.py --name csc-python-energy-intelligence \\
        --title "Greece Energy Intelligence Platform" \\
        --technology Python --level Intermediate --output ..

Sources of truth read at run time (all inside this library):
    docs/NAMING_AND_VERSIONING.md   technology identifiers and catalogue areas
    PROJECT_ROADMAP.md              approved projects (informational check)
    templates/                      README (English and Greek) and release notes templates
    LICENSE, .gitignore             copied / extended
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

LIBRARY = Path(__file__).resolve().parent.parent
TEMPLATES = LIBRARY / "templates"
NAMING = LIBRARY / "docs" / "NAMING_AND_VERSIONING.md"
ROADMAP = LIBRARY / "PROJECT_ROADMAP.md"

README_EN_TEMPLATE = TEMPLATES / "PROJECT_README_TEMPLATE.md"
README_EL_TEMPLATE = TEMPLATES / "PROJECT_README_EL_TEMPLATE.md"
NOTES_EN_TEMPLATE = TEMPLATES / "RELEASE_NOTES_TEMPLATE.md"
NOTES_EL_TEMPLATE = TEMPLATES / "RELEASE_NOTES_EL_TEMPLATE.md"
LICENSE_FILE = LIBRARY / "LICENSE"
GITIGNORE_BASE = LIBRARY / ".gitignore"

LEVELS = ("Foundation", "Intermediate", "Advanced")

GITATTRIBUTES = "# Keep line endings stable across Windows, macOS and Linux\n* text=auto eol=lf\n"

SECRETS_IGNORE = "\n# Local configuration and secrets must never be committed\n.env\n.env.*\n"

GITIGNORE_EXTRA = {
    "java": "\n# Java / Maven build output\ntarget/\nout/\n*.class\n*.iml\n.classpath\n.project\n.settings/\nhs_err_pid*.log\n",
    "python": (
        "\n# Python\n__pycache__/\n*.py[cod]\n.venv/\nvenv/\n.pytest_cache/\n.mypy_cache/\n"
        ".ruff_cache/\n*.egg-info/\ndist/\nbuild/\nhtmlcov/\n.coverage\n"
    ),
    "js": "\n# JavaScript / Node\nnode_modules/\ndist/\nbuild/\ncoverage/\n*.log\n",
    "mobile": (
        "\n# Flutter / Dart\n.dart_tool/\nbuild/\n.pub-cache/\n.pub/\n.flutter-plugins\n"
        ".flutter-plugins-dependencies\nlocal.properties\n*.iml\n"
    ),
    "generic": "",
}

# Technology keyword -> skeleton kind. The keyword that appears first in the
# --technology text wins (longer keyword on ties, so "javascript" beats "java").
KEYWORDS = (
    ("flutter", "mobile"), ("dart", "mobile"), ("python", "python"),
    ("javascript", "js"), ("typescript", "js"), ("html", "js"), ("java", "java"),
)


class ScaffoldError(Exception):
    """A validation or safety problem; the message is shown to the user."""


def read_text(path):
    if not path.is_file():
        raise ScaffoldError("Missing library file: %s" % path)
    with open(str(path), "r", encoding="utf-8") as handle:
        return handle.read()  # universal newlines: CRLF checkouts are normalised to LF


def area_table():
    """Technology identifier -> catalogue area, read from the naming standard."""
    areas = {}
    for line in read_text(NAMING).splitlines():
        match = re.match(r"^\|\s*([^|]+?)\s*\|\s*`([a-z0-9]+)`\s*\|\s*$", line)
        if match:
            areas[match.group(2)] = match.group(1)
    if not areas:
        raise ScaffoldError("No technology identifiers found in %s" % NAMING)
    return areas


def heading_levels(text):
    return [len(m.group(1)) for m in re.finditer(r"^(#{1,6}) ", text, re.MULTILINE)]


def replace_once(text, old, new, where):
    if text.count(old) != 1:
        raise ScaffoldError("Template %s no longer contains exactly one %r; update tools/new-project.py" % (where, old))
    return text.replace(old, new)


def skeleton_kind(technology):
    lowered = technology.lower()
    found = [(lowered.index(word), -len(word), kind) for word, kind in KEYWORDS if word in lowered]
    return min(found)[2] if found else "generic"


def skeleton_files(kind, name, prefix):
    """Empty, safe source/test folders. Returns {relative posix path: content}."""
    if kind == "java":
        return {"src/main/java/.gitkeep": "", "src/test/java/.gitkeep": ""}
    if kind == "python":
        package = name[len("csc-" + prefix + "-"):].replace("-", "_")
        if package[0].isdigit():
            package = "p_" + package
        return {"src/%s/__init__.py" % package: "", "tests/.gitkeep": ""}
    if kind == "mobile":
        return {}  # created by `flutter create .` / `dart create .` inside the repository
    return {"src/.gitkeep": "", "tests/.gitkeep": ""}


def roadmap_entry(name):
    if not ROADMAP.is_file():
        return None
    for line in read_text(ROADMAP).splitlines():
        if line.startswith("|") and ("`%s`" % name) in line:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 6:
                return {"order": cells[0], "title": cells[2], "level": cells[4], "status": cells[5]}
    return None


def build_plan(args, areas):
    name = args.name.strip()
    match = re.match(r"^csc-([a-z0-9]+)-([a-z0-9]+(?:-[a-z0-9]+)*)$", name)
    if not match:
        raise ScaffoldError("Invalid --name %r: use csc-<technology>-<project-name> in lowercase letters, digits and single hyphens" % name)
    prefix = match.group(1)
    if prefix not in areas:
        raise ScaffoldError("Unknown technology identifier %r in --name. Known identifiers (docs/NAMING_AND_VERSIONING.md): %s" % (prefix, ", ".join(sorted(areas))))
    title = " ".join(args.title.split())
    if not title or re.search(r"[<>\x00-\x1f]", args.title):
        raise ScaffoldError("Invalid --title: it must be non-empty and must not contain < or > or control characters")
    technology = " ".join(args.technology.split())
    if not technology:
        raise ScaffoldError("Invalid --technology: empty")
    level = next((l for l in LEVELS if l.lower() == args.level.strip().lower()), None)
    if level is None:
        raise ScaffoldError("Invalid --level %r: choose one of %s" % (args.level, ", ".join(LEVELS)))

    output = Path(args.output).expanduser()
    if not output.is_dir():
        raise ScaffoldError("--output %s is not an existing directory" % output)
    target = output.resolve() / name
    library = LIBRARY.resolve()
    if target == library or library in target.parents:
        raise ScaffoldError("Refusing to create a project inside the library repository (%s)" % library)
    if target.exists() or target.is_symlink():
        raise ScaffoldError("Refusing to touch existing path: %s" % target)

    area = areas[prefix]
    readme_en = read_text(README_EN_TEMPLATE)
    readme_el = read_text(README_EL_TEMPLATE)
    notes_en = read_text(NOTES_EN_TEMPLATE)
    notes_el = read_text(NOTES_EL_TEMPLATE)
    if heading_levels(readme_en) != heading_levels(readme_el):
        raise ScaffoldError("The English and Greek README templates no longer have the same heading structure; fix templates/ first")
    if heading_levels(notes_en) != heading_levels(notes_el):
        raise ScaffoldError("The English and Greek release notes templates no longer have the same heading structure; fix templates/ first")

    readme_en = replace_once(readme_en, "# CSC — <Project Title>", "# CSC — " + title, "PROJECT_README_TEMPLATE.md")
    readme_en = replace_once(readme_en, "`csc-<technology>-<project-name>`", "`%s`" % name, "PROJECT_README_TEMPLATE.md")
    readme_en = replace_once(readme_en, "<Catalogue area>", area, "PROJECT_README_TEMPLATE.md")
    readme_en = replace_once(readme_en, "<Foundation / Intermediate / Advanced — choose one>", level, "PROJECT_README_TEMPLATE.md")
    readme_en = replace_once(readme_en, "| <Language/runtime/framework/library/database> |", "| %s |" % technology, "PROJECT_README_TEMPLATE.md")

    readme_el = replace_once(readme_el, "# CSC — <Project Title>", "# CSC — " + title, "PROJECT_README_EL_TEMPLATE.md")
    readme_el = replace_once(readme_el, "`csc-<technology>-<project-name>`", "`%s`" % name, "PROJECT_README_EL_TEMPLATE.md")
    readme_el = replace_once(readme_el, "<Περιοχή καταλόγου>", area, "PROJECT_README_EL_TEMPLATE.md")
    readme_el = replace_once(readme_el, "<Foundation / Intermediate / Advanced — επιλέξτε ένα>", level, "PROJECT_README_EL_TEMPLATE.md")
    readme_el = replace_once(readme_el, "| <Γλώσσα/runtime/framework/βιβλιοθήκη/βάση δεδομένων> |", "| %s |" % technology, "PROJECT_README_EL_TEMPLATE.md")

    notes_en = replace_once(notes_en, "**<Project Title>**", "**%s**" % title, "RELEASE_NOTES_TEMPLATE.md")
    notes_en = replace_once(notes_en, "Level: <Foundation / Intermediate / Advanced>.", "Level: %s." % level, "RELEASE_NOTES_TEMPLATE.md")
    notes_el = replace_once(notes_el, "**<Project Title>**", "**%s**" % title, "RELEASE_NOTES_EL_TEMPLATE.md")
    notes_el = replace_once(notes_el, "Επίπεδο: <Foundation / Intermediate / Advanced>.", "Επίπεδο: %s." % level, "RELEASE_NOTES_EL_TEMPLATE.md")

    if not LICENSE_FILE.is_file():
        raise ScaffoldError("Missing library file: %s" % LICENSE_FILE)
    kind = skeleton_kind(technology)
    gitignore = read_text(GITIGNORE_BASE).rstrip("\n") + "\n" + GITIGNORE_EXTRA[kind] + SECRETS_IGNORE

    files = {
        "README.md": readme_el,
        "README.en.md": readme_en,
        "RELEASE_NOTES.md": notes_en,
        "RELEASE_NOTES.el.md": notes_el,
        ".gitignore": gitignore,
        ".gitattributes": GITATTRIBUTES,
        "docs/.gitkeep": "",
        "docs/screenshots/.gitkeep": "",
    }
    files.update(skeleton_files(kind, name, prefix))
    return {"name": name, "title": title, "level": level, "technology": technology, "area": area,
            "kind": kind, "target": target, "files": files, "prefix": prefix}


def write_project(plan):
    target = plan["target"]
    created_dir = False
    try:
        target.mkdir(parents=False, exist_ok=False)  # fails, instead of merging, if the path appeared meanwhile
        created_dir = True
        for rel, content in sorted(plan["files"].items()):
            path = target.joinpath(*rel.split("/"))
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(str(path), "w", encoding="utf-8", newline="\n") as handle:
                handle.write(content)
        shutil.copyfile(str(LICENSE_FILE), str(target / "LICENSE"))  # byte-for-byte copy
    except Exception:
        if created_dir:
            shutil.rmtree(str(target), ignore_errors=True)  # only the directory created by this run
        raise


def count_placeholders(plan):
    result = {}
    for rel in ("README.md", "README.en.md", "RELEASE_NOTES.md", "RELEASE_NOTES.el.md"):
        text = re.sub(r"<!--.*?-->", "", plan["files"][rel], flags=re.DOTALL)
        result[rel] = len([p for p in re.findall(r"<[^<>\n]+>", text) if p not in ("<br>",)])
    return result


def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="new-project.py",
        description="Create the boilerplate of a new CSC project repository from the library templates.",
        epilog='Example: python tools/new-project.py --name csc-python-energy-intelligence '
               '--title "Greece Energy Intelligence Platform" --technology Python --level Intermediate --output ..',
    )
    parser.add_argument("--name", required=True, help="repository name: csc-<technology>-<project-name>")
    parser.add_argument("--title", required=True, help="human-readable project title")
    parser.add_argument("--technology", required=True, help="primary language/technology, e.g. Python, Java, JavaScript, Flutter")
    parser.add_argument("--level", required=True, help="one of: " + ", ".join(LEVELS))
    parser.add_argument("--output", required=True, help="existing parent directory in which <name>/ is created")
    parser.add_argument("--dry-run", action="store_true", help="validate and list what would be created, write nothing")
    return parser.parse_args(argv)


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")  # non-UTF-8 Windows consoles must not crash on Greek text
        except (AttributeError, ValueError):
            pass
    args = parse_args(argv)
    try:
        areas = area_table()
        plan = build_plan(args, areas)
        entry = roadmap_entry(plan["name"])
        warnings = []
        if entry is None:
            warnings.append("%s is not in PROJECT_ROADMAP.md; add it there first (the roadmap is the source of truth)" % plan["name"])
        else:
            if entry["status"] != "Planned":
                warnings.append("roadmap status is %s, not Planned" % entry["status"])
            if plan["level"].lower() not in entry["level"].lower():
                warnings.append("level %s differs from the roadmap level %s" % (plan["level"], entry["level"]))
            if plan["title"].lower() != entry["title"].lower():
                warnings.append("title differs from the roadmap title %r" % entry["title"])
        if args.dry_run:
            print("Dry run: nothing written. Would create %s with:" % plan["target"])
            for rel in sorted(plan["files"]) + ["LICENSE"]:
                print("  " + rel)
        else:
            write_project(plan)
            print("Created %s" % plan["target"])
            for rel in sorted(plan["files"]) + ["LICENSE"]:
                print("  " + rel)
        for warning in warnings:
            print("WARNING: " + warning)
        remaining = count_placeholders(plan)
        print("Placeholders still to fill: " + ", ".join("%s=%d" % kv for kv in sorted(remaining.items())))
        if plan["kind"] == "mobile":
            print("Note: no source folders were created; run the framework generator inside the repository (e.g. flutter create .).")
        if not args.dry_run:
            print("Next: fill every placeholder, add real screenshots only from real runs, then in the new folder run "
                  "git init -b main, set repository-local user.name/user.email, git add, git commit. "
                  "No release, tag or push was made.")
        return 0
    except ScaffoldError as error:
        sys.stderr.write("ERROR: %s\n" % error)
        return 2


if __name__ == "__main__":
    sys.exit(main())
