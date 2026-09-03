---
name: delivery-program
description: Design and deliver evidence-backed programs for substantial work through one authorized slice at a time. Use when work needs a durable roadmap, explicit responsibility transitions, bounded implementation, staged review, and acceptance across multiple sessions. Do not use for a small local edit or a read-only assessment.
---

# Delivery Program

## Purpose

Turn a broad objective into a sequence of observable product increments without permitting the plan, implementation, or review process to become a second source of authority.

Keep one active slice. Make authorization explicit. Complete replacement work by migrating callers and retiring superseded authority rather than deferring cleanup.

## Operating Modes

Use `design` when the user asks to assess, architect, sequence, or prepare a program. Produce an approval-ready program and stop before implementation.

Use `delivery` only after explicit implementation authorization. Load the current program ledger and active-slice record. Repair a stale or contradictory design boundary before editing.

Use `single-slice` for one substantial bounded change. It uses an active-slice record without manufacturing a roadmap.

## Durable Artifact Topology

Maintain at most two primary delivery artifacts:

- the program ledger owns objective, backlog, maturity, decisions, authorization, active-slice selection, anomalies, and final reconciliation
- the active-slice record owns the frozen contract, responsibility dispositions, candidate evidence, staged judgments, corrections, and closeout

Assessments, manifests, test logs, and separate receipts are supporting evidence. Create them only when their independent identity has durable value. Worker and review packets are projections of the active-slice record, not new authorities.

Read:

- [maturity-model.md](references/maturity-model.md) before setting or reassessing maturity
- [program-ledger.md](references/program-ledger.md) before creating or advancing a program
- [active-slice.md](references/active-slice.md) before freezing, authorizing, or delivering a slice
- [assurance.md](references/assurance.md) before logical review, Style Assurance, Gate Acceptance, correction, or anomaly handling
- the bundled `assessment-by-domain` skill before cross-domain planning

Use [delivery_program.py](scripts/delivery_program.py) when its scaffold or structural validation reduces transcription drift.

## Non-Negotiable Controls

- Prefer the smallest change through existing architecture that proves the next observable behavior.
- Separate runtime participants, behavior-change owners, and likely write scope.
- Preserve accepted product proof, policy, limits, and user overrides verbatim.
- Treat new crates, stores, protocols, services, background runtimes, compatibility systems, and future-facing public abstractions as expansion requiring authority.
- Give every changed semantic responsibility a mode of `new`, `retain`, `extend`, `replace`, or `move`.
- A `replace` or `move` slice is not build-ready unless caller migration and retirement fit inside the same completed slice.
- Disconnection from one active route is not retirement. Inspect registrations, public exports, writer APIs, stores, recovery, compatibility, tests, and fuzz targets.
- Compatibility may preserve evidence-backed reading or forwarding. It may not preserve a second writer, planner, selector, coordinator, or decision authority.
- Passing tests does not excuse policy, authorization, maturity, or retirement failure.
- Acceptance, commit authority, and next-slice authority are separate facts.

## Design The Program

### Establish Current Ground

Read user-named sources, active policy, current code on the direct path, and one dependency hop. Separate implemented behavior, runtime wiring, intended design, and speculative future behavior.

Set a bounded investigation budget. Stop and lower confidence when it is exhausted rather than silently expanding discovery.

### Calibrate Maturity

Apply the maturity model to the affected initiative, not the whole repository. Use the least mature critical dimension to limit breadth and the highest current consequence as the obligation floor.

Record evidence, direct product proof, hard limits, tripwires, expansion gates, and user overrides. Maturity never relaxes active policy or replacement completeness.

### Trace Product And Responsibility

Trace one path from user or operator input to an observable outcome. For every changed responsibility, identify its semantic owner, current runtime entrypoint, real callers, registration, persistent state, intended mode, successor when applicable, and required proof.

Do not relabel a plan, event, diagnostic, test harness, or dormant library as the requested outcome.

When the concern crosses domains, run the canonical two-pass assessment. Freeze the affected-domain set before selecting write scope. Do not turn every runtime participant into an implementation target.

### Build The Ledger And Active Slice

Keep later work as backlog. Make only the smallest next product increment eligible for authorization.

Use exactly one readiness value:

- `assessment-only` when outcome, ownership, evidence, or disposition remains unresolved
- `approval-ready` when the design is complete but explicit authorization remains
- `build-ready` only when scope, policy obligations, responsibility dispositions, proof, limits, and authority are complete

Create the active-slice contract from [active-slice.md](references/active-slice.md). Applicable policy must be traced into deliverables and proof. Every incumbent surface must have an explicit disposition before replacement work becomes build-ready.

### Review And Authorize The Design

Run one integrated design review for product-path completeness, boundary correctness, policy traceability, maturity fit, responsibility disposition, and unnecessary architecture.

Freeze ordinary findings after the initial pass and permit one bounded verification by default. Material contradictory evidence is an anomaly and is never excluded merely because findings were frozen.

End design mode with readiness, unresolved decisions, exact authorized and unauthorized actions, and an explicit statement that implementation has not started.

## Deliver The Active Slice

### Start Cleanly

Confirm the active-slice identity, authorization register, branch, worktree, policies, candidate baseline, and applicable disposition rows. Do not absorb unrelated changes.

Compare the estimated change surface with every hard limit, tripwire, and retirement anomaly before editing.

### Implement Vertically

Give the implementor a projection of the active-slice record containing direct behavior, applicable responsibility rows, policy obligations, write scope, reuse seams, non-goals, limits, proof, and stop conditions.

The implementor may simplify or report a missing boundary. It may not change responsibility mode, relax limits, approve expansion, retain a superseded authority, or infer later authorization.

### Prove The Candidate

Run direct product proof first. Add broader validation only where policy, changed surface, persistence, compatibility, or operational risk requires it.

Record candidate identity and the actual complexity delta. For a replacement, no production deletion or unexpectedly small retirement is a mandatory anomaly review, not an automatic failure and not a fixed ratio.

### Judge In Three Passes

Use three ordered judgments over the same candidate:

- logical review asks whether the slice behaves correctly and satisfies scope, policy, ownership, and responsibility disposition
- Style Assurance asks whether the logically accepted candidate satisfies commenting, structure, formatting, lint, and risk-proportionate test quality
- Gate Acceptance asks whether the declared deliverables compose across the frozen handoff boundary

Keep these questions separate without requiring separate durable receipt files. Record each verdict and its evidence in the active-slice record. A failed or changed earlier pass invalidates eligibility for later passes.

Use one initial pass and one bounded correction and verification cycle per judgment by default. Do not stack redundant reviews over the same question.

### Handle Contradictory Evidence

New material evidence may reopen any prior judgment. Record an anomaly, identify the earliest invalid boundary, invalidate dependent verdicts, and classify the cause as design-contract defect, implementation defect, evidence defect, unauthorized scope, or authorized exception.

Freeze limits correction scope. It does not make accepted claims immune to contradiction.

### Commit And Advance

Commit only when the active slice is accepted and the user and repository policy authorize it. Record a plain-language Commit Effect beginning with `If applied, this commit`.

Mark a slice complete only after required commit and closeout. Activate the next slice only through explicit authority recorded separately from acceptance.

## Closeout

Report the behavior proved, responsibility dispositions, retirement evidence, complexity delta, expansions, staged judgments, corrections, anomalies, exceptions, commit state, unauthorized backlog, unresolved risks, and worktree state.

Claim only the directly proved product behavior. Do not claim a roadmap complete because its internal artifacts exist.
