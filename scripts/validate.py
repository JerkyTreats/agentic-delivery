#!/usr/bin/env python3
"""Validate the plugin repository with only the Python standard library."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"\[[^]]+\]\(([^)]+)\)")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"missing frontmatter: {path}", errors)
        return {}
    try:
        raw = text.split("---\n", 2)[1]
    except IndexError:
        fail(f"unterminated frontmatter: {path}", errors)
        return {}
    values: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def validate_links(path: Path, errors: list[str]) -> None:
    for link in LINK_PATTERN.findall(path.read_text(encoding="utf-8")):
        if "://" in link or link.startswith("#"):
            continue
        target = link.split("#", 1)[0]
        if target and not (path.parent / target).exists():
            fail(f"broken relative link in {path}: {link}", errors)


def main() -> None:
    errors: list[str] = []
    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for key in ("name", "version", "description", "author", "skills", "interface"):
        if key not in manifest:
            fail(f"plugin manifest missing {key}", errors)
    if manifest.get("name") != ROOT.name:
        fail("plugin name must match repository directory", errors)
    if "mcpServers" in manifest:
        fail("skills-only plugin must not declare MCP servers", errors)

    expected = {"assessment-by-domain", "delivery-program"}
    actual = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    if actual != expected:
        fail(f"unexpected skill set: {sorted(actual)}", errors)

    for skill_name in sorted(expected):
        skill_root = ROOT / "skills" / skill_name
        skill_md = skill_root / "SKILL.md"
        values = frontmatter(skill_md, errors)
        if values.get("name") != skill_name:
            fail(f"skill name mismatch: {skill_md}", errors)
        unfinished_word = "TO" + "DO"
        if not values.get("description") or unfinished_word in values.get("description", ""):
            fail(f"skill description incomplete: {skill_md}", errors)
        metadata = skill_root / "agents" / "openai.yaml"
        if not metadata.is_file():
            fail(f"missing UI metadata: {metadata}", errors)
        elif f"${skill_name}" not in metadata.read_text(encoding="utf-8"):
            fail(f"default prompt must mention ${skill_name}: {metadata}", errors)
        validate_links(skill_md, errors)
        for reference in (skill_root / "references").glob("*.md") if (skill_root / "references").exists() else ():
            validate_links(reference, errors)

    unfinished_marker = "[" + "TODO:"
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if unfinished_marker in text:
                fail(f"unfinished scaffold marker: {path}", errors)

    helper = ROOT / "skills" / "delivery-program" / "scripts" / "delivery_program.py"
    result = subprocess.run(
        [sys.executable, str(helper), "--help"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        fail(f"delivery helper failed --help: {result.stderr.strip()}", errors)

    if errors:
        for error in errors:
            print(f"error: {error}")
        raise SystemExit(1)
    print("repository validation passed")


if __name__ == "__main__":
    main()
