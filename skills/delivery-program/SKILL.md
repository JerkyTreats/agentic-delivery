---
name: delivery-program
description: Design and execute evidence-backed delivery programs for substantial, long-horizon work. Use when a broad objective needs an architecture assessment, maturity-calibrated phases, explicit authorization gates, a durable program ledger, bounded implementation slices, integrated review, and closeout across multiple commits or work sessions. Do not use for a small local edit or a read-only domain assessment.
---

# Delivery Program

## Purpose

Turn broad intent into an authorized sequence of product increments, then deliver one active slice at a time through the smallest architecture supported by current evidence.

Keep design authority, implementation authority, and roadmap detail separate. A thorough plan does not authorize every phase.

## Select The Operating Mode

Use `design` mode when the user asks to assess, architect, sequence, or prepare a program. Produce an approval-ready ledger and stop before implementation.

Use `delivery` mode only when the user explicitly authorizes implementation. Load an existing ledger when present. If the ledger is missing or stale, repair the design boundary before editing.

Use `single-slice` mode for one substantial bounded implementation. It follows the same gates without manufacturing a multi-phase roadmap.

Do not use this skill for a small local change whose scope, proof, and ownership are already obvious.

## Load Guidance Progressively

- Read [maturity-model.md](references/maturity-model.md) before setting or reassessing the maturity envelope.
- Read [program-ledger.md](references/program-ledger.md) before creating, validating, or advancing a program ledger.
- Read [phase-packets.md](references/phase-packets.md) before delegating implementation or review.
- Read [vertical-delivery.md](references/vertical-delivery.md) when activating or implementing a product slice.
- Read the bundled `assessment-by-domain` skill before a cross-domain assessment. Preserve its frozen affected set as program evidence.
- Use [delivery_program.py](scripts/delivery_program.py) when a deterministic ledger or packet scaffold would reduce transcription drift.

Read only the guidance needed for the active operation.

## Shared Invariants

- Prefer the smallest change through existing architecture that proves the next externally observable behavior.
- Separate domains on the product path, domains whose behavior changes, and files likely to change.
- Preserve accepted limits, direct product proof, and user overrides verbatim.
- Treat new crates, durable stores, protocols, services, background runtimes, compatibility systems, and future-facing public abstractions as architectural expansion.
- Require explicit approval for expansion not already authorized by the maturity envelope.
- Keep later phases as uncommitted backlog.
- Use one active slice, one review owner, one initial review, and one verification pass by default.
- Passing tests does not excuse an authorization, policy, or maturity-envelope violation.
- Follow the active host and repository policies for branches, worktrees, commits, approvals, and delegation.

## Design A Program

### Establish Current Ground

Read user-named sources, active policy, current code on the direct path, and one dependency hop. Separate implemented behavior, runtime wiring, design intent, and speculative future behavior.

Set an investigation budget before broad discovery. Stop when the budget is exhausted and lower confidence instead of silently expanding it.

### Calibrate Maturity

Apply the maturity model to the requested initiative rather than to the whole repository. Use the least mature critical dimension to limit solution breadth and the highest current consequence as the obligation floor.

Record a visible maturity envelope with evidence, product proof, hard limits, tripwires, approval gates, investigation budget, review owner, and review budget. Keep inferred values provisional until the user accepts them.

### Trace The Product Path

Trace one path from user or operator input to an observable outcome. For each hop, identify the current anchor, missing behavior, existing seam, minimum state, and acceptance evidence.

Do not relabel an internal plan, event, diagnostic, library proof, or harness artifact as the requested product outcome. A prerequisite experiment is non-delivery evidence unless it completes the accepted trace.

### Assess By Domain

Run the canonical two-pass assessment when the concern crosses ownership boundaries. Freeze the affected-domain set before planning. Do not convert every traversed domain into implementation scope.

### Build The Program Ledger

Make only the first product slice build-ready. Record later work as backlog with dependencies and activation evidence.

Use exactly one readiness label:

- `build-ready` when the envelope is accepted, required expansion is approved, scope is exact, and review has no blocker
- `approval-ready` when the program is complete but a named architectural or scope decision remains
- `assessment-only` when the terminal behavior, ownership, evidence, or exact scope remains unresolved

For every slice record its product increment, exact acceptance evidence, owned change scope, existing seams, dependencies, expansion decisions, stop conditions, and closeout evidence.

### Review The Design

Use one integrated review lane for product-path completeness, boundary correctness, maturity fit, and unnecessary architecture. Freeze findings after the initial pass. Run at most one verification pass after accepted corrections.

A design finding blocks only for missing product proof, incorrect active-path behavior, concrete current data or security risk, applicable policy violation, or maturity-envelope violation.

End design mode with the ledger, readiness, unresolved decisions, and an explicit statement that implementation has not started.

## Deliver The Authorized Program

### Start Cleanly

Confirm the authorized boundary, current branch, worktree state, applicable policies, and active slice. Create a feature branch when policy and user intent require one. Do not absorb unrelated dirty changes.

Treat explicit delivery authorization as authority for normal implementation mechanics inside the accepted envelope when host and repository policy permit them. It is not authority for architectural expansion or later backlog phases.

### Activate One Slice

Choose the smallest authorized slice that produces a direct observable increment. Compare its estimated change surface with every tripwire before editing.

If the next phase is only substrate, compatibility, migration, or generalized infrastructure, require evidence that the active product path needs it now.

### Implement Vertically

Follow the vertical-delivery guidance. Prefer one implementor at exploratory and first-slice maturity. Add parallel workers only when delegation is permitted, scopes are disjoint, and the accepted envelope allows it.

Every worker receives the maturity envelope, direct product proof, affected-domain set, write scope, forbidden changes, tests, approval gates, tripwires, review owner, and stop conditions. Workers may simplify or report a missing boundary. They may not raise maturity, relax limits, or approve expansion.

### Integrate And Prove

Inspect returned work for scope compliance before integration. Run direct acceptance evidence first, then only the broader gates required by policy, changed surface, or current operational stakes.

Record the actual complexity delta:

- files and lines changed
- dependencies or workspace members added
- public contracts added
- stores or schemas added
- background runtimes added
- product behavior proved

Crossing a tripwire pauses integration until the user disposes it.

### Review Once

The program owns integrated review. Do not stack leaf, slice, and program reviews over the same diff.

Freeze the initial finding set. Fix accepted blockers within the active slice, then run one verification limited to those findings and regressions caused by their fixes. Record remaining disagreement as risk or request one user decision.

### Commit And Advance

Commit accepted work after proof and required gates pass when user intent and repository policy permit it. Before each delivery commit, record a plain-language Commit Effect beginning with `If applied, this commit`.

Reassess maturity only from evidence created by completed behavior, a new real consumer, an observed failure, or a changed operational obligation.

Advance only when the next slice is already authorized, remains inside the accepted envelope, and directly advances observable behavior. Otherwise stop for user authorization.

## Closeout

Close only the authorized scope. Report:

- behavior proved
- maturity evidence gained
- complexity delta
- expansion decisions
- tests and gates
- review findings and verification
- commits or no-commit exception
- backlog still unauthorized
- unresolved risks
- clean or dirty worktree state

Do not claim a roadmap complete because its internal phases were implemented. Claim only the product behavior directly proved.
