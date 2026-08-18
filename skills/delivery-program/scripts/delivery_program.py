#!/usr/bin/env python3
"""Scaffold and validate delivery-program ledgers and bounded packets."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


REQUIRED_LEDGER_HEADINGS = (
    "## Objective And Product Proof",
    "## Maturity Envelope",
    "## Authorized Active Slice",
    "## Uncommitted Backlog",
    "## Product Trace",
    "## Affected Domains",
    "## Expansion Decisions",
    "## Hard Limits And Tripwires",
    "## Phase Inventory",
    "## Work State",
    "## Gate Evidence",
    "## Complexity Delta",
    "## Commit Effects",
    "## Review State",
    "## Risks And Exceptions",
    "## Reassessment",
    "## Final Reconciliation",
)


def write_new(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit(f"refusing to overwrite existing file: {path}")
    path.write_text(content, encoding="utf-8")


def init_ledger(args: argparse.Namespace) -> None:
    content = dedent(
        f"""\
        # Delivery Program Ledger

        Date: {args.date}
        Branch: {args.branch}
        Status: {args.status}
        Readiness: {args.readiness}

        ## Objective And Product Proof

        Objective: {args.objective}

        Direct product proof: {args.product_proof}

        Acceptance evidence: {args.acceptance_evidence}

        Explicit non-goals: {args.non_goals}

        Applicable policy: {args.policies}

        ## Maturity Envelope

        Posture: {args.posture}

        Obligation floor: {args.obligation_floor}

        Confidence and evidence: {args.maturity_evidence}

        User override: {args.user_override}

        Approval gates: {args.approval_gates}

        Review owner and budget: {args.review_budget}

        ## Authorized Active Slice

        None until explicitly activated.

        ## Uncommitted Backlog

        ## Product Trace

        ## Affected Domains

        ## Expansion Decisions

        ## Hard Limits And Tripwires

        Hard limits: {args.hard_limits}

        Tripwires: {args.tripwires}

        ## Phase Inventory

        | Phase | Product increment | Dependency | Status | Proof |
        | --- | --- | --- | --- | --- |

        ## Work State

        | Slice | Branch or worktree | Owner | Status | Commit | Notes |
        | --- | --- | --- | --- | --- | --- |

        ## Gate Evidence

        | Gate | Command or observation | Result | Date | Notes |
        | --- | --- | --- | --- | --- |

        ## Complexity Delta

        ## Commit Effects

        ## Review State

        Initial findings: not run

        Verification: not run

        ## Risks And Exceptions

        ## Reassessment

        ## Final Reconciliation
        """
    )
    target = Path(args.path)
    write_new(target, content)
    print(target)


def validate_ledger(args: argparse.Namespace) -> None:
    target = Path(args.path)
    if not target.is_file():
        raise SystemExit(f"ledger does not exist: {target}")
    content = target.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED_LEDGER_HEADINGS if heading not in content]
    if missing:
        for heading in missing:
            print(f"missing: {heading}")
        raise SystemExit(1)
    if "Direct product proof:" not in content:
        print("missing: Direct product proof")
        raise SystemExit(1)
    print(f"valid: {target}")


def worker_packet(args: argparse.Namespace) -> None:
    print(
        dedent(
            f"""\
            Objective:
            {args.objective}

            Active slice:
            {args.active_slice}

            Direct product proof:
            {args.product_proof}

            Maturity envelope:
            {args.maturity_envelope}

            Frozen affected-domain set:
            {args.affected_domains}

            Hard limits and tripwires:
            {args.limits}

            Approval gates and approved expansions:
            {args.approvals}

            Write scope:
            {args.write_scope}

            Read scope:
            {args.read_scope}

            Existing seams to reuse:
            {args.existing_seams}

            Explicit non-goals:
            {args.non_goals}

            Required proof and gates:
            {args.gates}

            Review owner:
            {args.review_owner}

            Forbidden changes:
            {args.forbidden}

            Stop before unapproved expansion. Stop and report any tripwire breach.
            Do not raise maturity, relax limits, or reinterpret the product proof.

            Return changed files, direct proof, gate results, complexity delta,
            commits or exception, and unresolved risks.
            """
        )
    )


def review_packet(args: argparse.Namespace) -> None:
    print(
        dedent(
            f"""\
            Review pass: {args.review_pass}
            Review owner: {args.review_owner}

            Objective:
            {args.objective}

            Active slice and direct proof:
            {args.active_slice}

            Maturity envelope:
            {args.maturity_envelope}

            Diff or commit range:
            {args.diff}

            Complexity delta:
            {args.complexity_delta}

            Expansion decisions:
            {args.expansion_decisions}

            Gate evidence:
            {args.gate_evidence}

            Applicable policy:
            {args.policies}

            Accepted finding identifiers:
            {args.accepted_findings}

            Return findings only for active-path correctness, current data or security risk,
            applicable policy, and maturity fit. Freeze finding identifiers during an initial
            pass. During verification, assess only accepted findings and regressions caused by
            their fixes.
            """
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init-ledger", help="create a new program ledger")
    init.add_argument("--path", required=True)
    init.add_argument("--date", required=True)
    init.add_argument("--branch", default="not created")
    init.add_argument("--status", default="proposed")
    init.add_argument(
        "--readiness",
        choices=("assessment-only", "approval-ready", "build-ready"),
        default="assessment-only",
    )
    init.add_argument("--objective", required=True)
    init.add_argument("--product-proof", required=True)
    init.add_argument("--acceptance-evidence", required=True)
    init.add_argument("--non-goals", default="none recorded")
    init.add_argument("--policies", default="active repository and host policy")
    init.add_argument("--posture", required=True)
    init.add_argument("--obligation-floor", required=True)
    init.add_argument("--maturity-evidence", required=True)
    init.add_argument("--user-override", default="none")
    init.add_argument("--approval-gates", required=True)
    init.add_argument("--review-budget", required=True)
    init.add_argument("--hard-limits", required=True)
    init.add_argument("--tripwires", required=True)
    init.set_defaults(handler=init_ledger)

    validate = commands.add_parser("validate-ledger", help="check required ledger sections")
    validate.add_argument("--path", required=True)
    validate.set_defaults(handler=validate_ledger)

    worker = commands.add_parser("worker-packet", help="render a bounded worker packet")
    worker.add_argument("--objective", required=True)
    worker.add_argument("--active-slice", required=True)
    worker.add_argument("--product-proof", required=True)
    worker.add_argument("--maturity-envelope", required=True)
    worker.add_argument("--affected-domains", default="not applicable")
    worker.add_argument("--limits", required=True)
    worker.add_argument("--approvals", required=True)
    worker.add_argument("--write-scope", required=True)
    worker.add_argument("--read-scope", default="repository evidence needed by the slice")
    worker.add_argument("--existing-seams", required=True)
    worker.add_argument("--non-goals", default="none recorded")
    worker.add_argument("--gates", required=True)
    worker.add_argument("--review-owner", required=True)
    worker.add_argument("--forbidden", default="out-of-scope edits and unauthorized expansion")
    worker.set_defaults(handler=worker_packet)

    review = commands.add_parser("review-packet", help="render an initial or verification packet")
    review.add_argument("--review-pass", choices=("initial", "verification"), required=True)
    review.add_argument("--review-owner", required=True)
    review.add_argument("--objective", required=True)
    review.add_argument("--active-slice", required=True)
    review.add_argument("--maturity-envelope", required=True)
    review.add_argument("--diff", required=True)
    review.add_argument("--complexity-delta", required=True)
    review.add_argument("--expansion-decisions", default="none")
    review.add_argument("--gate-evidence", required=True)
    review.add_argument("--policies", default="active repository and host policy")
    review.add_argument("--accepted-findings", default="not applicable")
    review.set_defaults(handler=review_packet)

    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
