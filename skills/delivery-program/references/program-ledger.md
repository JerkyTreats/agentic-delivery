# Program Ledger

The ledger preserves program direction and authority across sessions. Keep detailed candidate evidence inside the active-slice record rather than duplicating it here.

## Required Contents

- objective and direct product proof
- maturity envelope and accepted overrides
- current product and responsibility trace
- frozen affected-domain set when applicable
- active-slice identifier and link
- backlog with dependencies and activation evidence
- architectural expansion decisions
- hard limits and program tripwires
- authorization register
- decision log
- anomaly and supersession log
- slice outcomes and commit effects
- reassessment and final reconciliation

## Lifecycle And Authority

Use a compact lifecycle:

- `backlog`
- `active`
- `blocked`
- `accepted`
- `complete`
- `superseded`

Readiness is separate and uses `assessment-only`, `approval-ready`, or `build-ready`.

For every authorization record:

- authorized action
- authority source
- exact scope
- activation date or candidate identity
- expiry or next approval boundary
- approved exceptions
- actions that remain unauthorized

Acceptance never implies commit, push, deployment, or next-slice authority.

## Backlog

Record later product increments with their outcome, current dependency, and activation evidence. Do not make their worker packets or gates acceptance-ready.

A detailed future design may inform the program but does not create implementation authority.

## Evidence And Decisions

Use current code, runtime wiring, tests, observations, authoritative policy, commits, user decisions, or explicit exceptions as evidence.

Record decisions that change scope, responsibility ownership, maturity, sequence, or authorization. Link rather than copy supporting assessments.

Do not use plan volume, test count, reviewer confidence, or internal infrastructure as evidence of product maturity.

## Anomalies And Supersession

Record material evidence that contradicts a frozen contract or accepted claim. Name the affected slice, obligation, earliest invalid boundary, dependent verdicts, disposition authority, and successor state.

Never silently edit history to make a failed claim appear correct. Preserve useful evidence while marking invalid acceptance or design authority as superseded.

## Advancement

Before selecting another slice, record:

- completed or accepted prior outcome
- exact remaining product gap
- continued validity of the maturity envelope
- unresolved replacement or compatibility obligations
- crossed limits or anomalies
- explicit activation authority

When authority is absent, the next task is design or approval, not implementation.
