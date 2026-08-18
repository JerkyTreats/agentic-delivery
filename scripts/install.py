#!/usr/bin/env python3
"""Link Agentic Delivery skills into user-level agent skill roots."""

from __future__ import annotations

import argparse
from pathlib import Path


TARGETS = {
    "codex": Path.home() / ".agents" / "skills",
    "claude": Path.home() / ".claude" / "skills",
    "pi": Path.home() / ".pi" / "agent" / "skills",
}


def install_into(source_root: Path, destination_root: Path) -> None:
    destination_root.mkdir(parents=True, exist_ok=True)
    for source in sorted(path for path in source_root.iterdir() if path.is_dir()):
        destination = destination_root / source.name
        if destination.is_symlink() and destination.resolve() == source.resolve():
            print(f"already linked: {destination}")
            continue
        if destination.exists() or destination.is_symlink():
            raise SystemExit(
                f"refusing to replace existing skill path: {destination}\n"
                "move or archive that path, then run the installer again"
            )
        destination.symlink_to(source, target_is_directory=True)
        print(f"linked: {destination} -> {source}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target",
        action="append",
        choices=sorted(TARGETS),
        default=[],
        help="known user skill root to install into; repeat as needed",
    )
    parser.add_argument(
        "--root",
        action="append",
        type=Path,
        default=[],
        help="additional compatible user skill root; repeat as needed",
    )
    args = parser.parse_args()

    roots = [TARGETS[name] for name in args.target] + [path.expanduser() for path in args.root]
    if not roots:
        parser.error("provide at least one --target or --root")

    repository = Path(__file__).resolve().parents[1]
    source_root = repository / "skills"
    for root in roots:
        install_into(source_root, root)

    legacy = Path.home() / ".codex" / "skills"
    conflicts = [legacy / skill.name for skill in source_root.iterdir() if (legacy / skill.name).exists()]
    if conflicts:
        print("legacy skill copies still exist and may create duplicate catalog entries:")
        for conflict in conflicts:
            print(f"  {conflict}")


if __name__ == "__main__":
    main()
