# Initiative Maturity Model

Apply maturity to the affected initiative rather than the repository as a whole.

Define the initiative as the requested change plus every current product path, durable record, consumer, and operational contract it can mutate or invalidate.

## Evidence Dimensions

Assess:

- product proof
- real consumer evidence
- semantic stability
- operational exposure
- observed failures
- persistence stakes
- integration depth

Design detail, test volume, implementation sophistication, and confidence are not maturity evidence.

## Posture

Use the least mature critical dimension to limit solution breadth. Record the highest current consequence separately as the obligation floor.

### Exploratory

The end-to-end behavior is unproved or core semantics remain unsettled. Prefer one reversible path through existing architecture. Require approval for new stores, protocols, services, migrations, and public generality.

### First Slice

One narrow path works but consumers or contracts remain unstable. Extend the proved path and add only durability required by current evidence.

### Repeated Use

Several real paths expose stable shared behavior or recurring failure. Bounded shared contracts and migrations may be justified by those consumers.

### Operational

Real users, durable data, security exposure, upgrades, or service obligations require explicit recovery, compatibility, observability, and hardening.

Maturity never relaxes policy, canonical ownership, replacement completeness, or authorization.

## Envelope

Record:

- posture and confidence
- evidence and obligation floor
- direct product proof
- user overrides
- forbidden expansions
- hard limits and tripwires
- investigation and review budgets when useful
- approval boundaries

Budgets are working constraints, not architecture evidence. Keep them out of durable records when they add no decision value.

## Expansion Test

Treat a new crate, durable store, cross-domain protocol, service, background runtime, compatibility system, migration mechanism, or future-facing public abstraction as expansion.

Require the current behavior it unblocks, evidence that existing architecture cannot provide it, current consumers, a simpler alternative, and explicit authority.

## Reassessment

Reassess only after completed behavior, a new real consumer, an observed failure, or a changed operational obligation. A more detailed plan does not raise maturity.
