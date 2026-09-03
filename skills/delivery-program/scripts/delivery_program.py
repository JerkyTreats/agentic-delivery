#!/usr/bin/env python3
"""Create and structurally validate delivery-program records."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


LEDGER_HEADINGS = (
    "## Objective And Product Proof",
    "## Maturity Envelope",
    "## Product And Responsibility Trace",
    "## Active Slice",
    "## Backlog",
    "## Authorization Register",
    "## Decisions",
    "## Anomalies And Supersession",
    "## Slice Outcomes",
    "## Reassessment And Reconciliation",
)

SLICE_HEADINGS = (
    "## Product Contract",
    "## Authorization",
    "## Maturity And Scope",
    "## Responsibility Disposition",
    "## Policy Trace",
    "## Proof And Retirement Evidence",
    "## Limits And Stop Conditions",
    "## Candidate And Complexity",
    "## Logical Review",
    "## Style Assurance",
    "## Gate Acceptance",
    "## Anomalies And Corrections",
    "## Closeout",
)


def write_new(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit(f"refusing to overwrite existing file: {path}")
    path.write_text(content, encoding="utf-8")


def read_validated(path: Path, headings: tuple[str, ...]) -> str:
    if not path.is_file():
        raise SystemExit(f"record does not exist: {path}")
    content = path.read_text(encoding="utf-8")
    missing = [heading for heading in headings if heading not in content]
    if missing:
        for heading in missing:
            print(f"missing: {heading}")
        raise SystemExit(1)
    return content


def validate(path: Path, headings: tuple[str, ...]) -> None:
    read_validated(path, headings)
    print(f"structurally valid: {path}")


def section(content: str, heading: str) -> str:
    remainder = content.split(heading, 1)[1]
    return remainder.split("\n## ", 1)[0]


def has_table_row(content: str, heading: str) -> bool:
    rows = [line for line in section(content, heading).splitlines() if line.startswith("|")]
    return len(rows) > 2


def validate_slice(path: Path) -> None:
    content = read_validated(path, SLICE_HEADINGS)
    errors: list[str] = []
    if "Readiness: build-ready" in content:
        if "Authorized action: none" in content or "Authority source: none" in content:
            errors.append("build-ready slice has no explicit authority")
        if not has_table_row(content, "## Responsibility Disposition"):
            errors.append("build-ready slice has no responsibility disposition")
        if not has_table_row(content, "## Policy Trace"):
            errors.append("build-ready slice has no policy trace")
        if "assessment required" in content.lower():
            errors.append("build-ready slice retains an unresolved assessment")
    if errors:
        for error in errors:
            print(f"invalid: {error}")
        raise SystemExit(1)
    print(f"structurally valid: {path}")


def init_ledger(args: argparse.Namespace) -> None:
    content = dedent(
        f"""\
        # Delivery Program Ledger

        Date: {args.date}
        Lifecycle: backlog
        Readiness: {args.readiness}

        ## Objective And Product Proof

        Objective: {args.objective}

        Direct product proof: {args.product_proof}

        ## Maturity Envelope

        Posture: {args.posture}

        Obligation floor: {args.obligation_floor}

        Evidence: {args.maturity_evidence}

        ## Product And Responsibility Trace

        ## Active Slice

        None selected.

        ## Backlog

        ## Authorization Register

        | Action | Authority | Scope | Boundary | Exceptions | Unauthorized |
        | --- | --- | --- | --- | --- | --- |

        ## Decisions

        ## Anomalies And Supersession

        ## Slice Outcomes

        ## Reassessment And Reconciliation
        """
    )
    target = Path(args.path)
    write_new(target, content)
    print(target)


def init_slice(args: argparse.Namespace) -> None:
    content = dedent(
        f"""\
        # Active Slice {args.slice_id}

        Date: {args.date}
        Baseline: {args.baseline}
        Lifecycle: active
        Readiness: {args.readiness}

        ## Product Contract

        Observable behavior: {args.product_behavior}

        Direct proof: {args.direct_proof}

        ## Authorization

        Authorized action: {args.authorized_action}

        Authority source: {args.authority_source}

        Actions still unauthorized: {args.unauthorized}

        ## Maturity And Scope

        ## Responsibility Disposition

        | Responsibility | Mode | Current route and state | Successor | Superseded surface | Final disposition | Proof | Exception |
        | --- | --- | --- | --- | --- | --- | --- | --- |

        ## Policy Trace

        | Policy obligation | Applies when | Responsibility | Deliverable | Proof | Exception authority |
        | --- | --- | --- | --- | --- | --- |

        ## Proof And Retirement Evidence

        ## Limits And Stop Conditions

        ## Candidate And Complexity

        ## Logical Review

        Verdict: not run

        ## Style Assurance

        Verdict: not eligible

        ## Gate Acceptance

        Verdict: not eligible

        ## Anomalies And Corrections

        ## Closeout
        """
    )
    target = Path(args.path)
    write_new(target, content)
    print(target)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    ledger = commands.add_parser("init-ledger", help="create a concise program ledger")
    ledger.add_argument("--path", required=True)
    ledger.add_argument("--date", required=True)
    ledger.add_argument(
        "--readiness",
        choices=("assessment-only", "approval-ready", "build-ready"),
        default="assessment-only",
    )
    ledger.add_argument("--objective", required=True)
    ledger.add_argument("--product-proof", required=True)
    ledger.add_argument("--posture", required=True)
    ledger.add_argument("--obligation-floor", required=True)
    ledger.add_argument("--maturity-evidence", required=True)
    ledger.set_defaults(handler=init_ledger)

    slice_record = commands.add_parser(
        "init-slice", help="create one active-slice contract and delivery record"
    )
    slice_record.add_argument("--path", required=True)
    slice_record.add_argument("--slice-id", required=True)
    slice_record.add_argument("--date", required=True)
    slice_record.add_argument("--baseline", required=True)
    slice_record.add_argument(
        "--readiness",
        choices=("assessment-only", "approval-ready", "build-ready"),
        default="assessment-only",
    )
    slice_record.add_argument("--product-behavior", required=True)
    slice_record.add_argument("--direct-proof", required=True)
    slice_record.add_argument("--authorized-action", default="none")
    slice_record.add_argument("--authority-source", default="none")
    slice_record.add_argument("--unauthorized", default="implementation and advancement")
    slice_record.set_defaults(handler=init_slice)

    validate_ledger = commands.add_parser(
        "validate-ledger", help="check the program-ledger structure"
    )
    validate_ledger.add_argument("--path", required=True)
    validate_ledger.set_defaults(
        handler=lambda args: validate(Path(args.path), LEDGER_HEADINGS)
    )

    validate_slice_parser = commands.add_parser(
        "validate-slice", help="check the active-slice structure"
    )
    validate_slice_parser.add_argument("--path", required=True)
    validate_slice_parser.set_defaults(
        handler=lambda args: validate_slice(Path(args.path))
    )

    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
