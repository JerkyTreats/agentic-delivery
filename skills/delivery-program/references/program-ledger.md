# Program Ledger

Use a concise ledger to preserve authority, maturity, product proof, and delivery state across work sessions.

## Required Sections

- objective and direct product proof
- maturity envelope and user overrides
- authorized active slice
- uncommitted backlog
- current product trace
- frozen affected-domain set when applicable
- architectural expansion decisions
- hard limits and tripwires
- phase and dependency inventory
- worker and worktree state
- gate and product-proof evidence
- complexity delta
- commit effects
- review owner and budget
- frozen findings and verification result
- risks and exceptions
- next-slice reassessment
- final reconciliation

## Phase Status

Use:

- `backlog`
- `proposed`
- `awaiting approval`
- `ready`
- `in progress`
- `integrating`
- `proof failed`
- `review failed`
- `complete`
- `deferred`
- `rejected`

Detailed source plans remain backlog until their next slice is explicitly activated.

## Evidence Standard

Point to current code, product traces, commits, tests, runtime observations, user evidence, authoritative policy, or explicit exceptions.

Do not use plan detail, test count, reviewer confidence, or implemented infrastructure as evidence that maturity increased.

## Expansion Decisions

For every proposed architectural expansion record:

- direct product behavior unblocked
- existing approach considered
- current consumers
- envelope authority or user approval
- disposition

## Complexity Delta

After each slice record:

- changed files
- lines added and removed
- new crates and dependencies
- new public contracts
- new stores and schemas
- new background runtimes
- direct product behaviors proved

Crossing a tripwire changes the slice status to `awaiting approval` until explicitly resolved.

## Review State

Record one review owner for the active slice. Embedded workers do not own review.

Record the initial frozen finding set and one verification result. Do not append unrelated findings during verification.

## Commit Gate

Commit accepted work after direct product proof and selected gates pass when user intent and repository policy permit it.

Before each delivery commit, record one Commit Effect beginning with `If applied, this commit`.

Do not create ledger-only launch or closeout commits unless policy or the user requires them.

## Advancement Gate

Before activating the next slice record:

- new maturity evidence from completed behavior
- whether the accepted envelope still applies
- whether the next slice directly advances product behavior
- any approval gate or tripwire crossed
- explicit authorization state
