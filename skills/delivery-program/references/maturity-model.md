# Initiative Maturity Model

## Contents

- Evidence dimensions
- Posture and obligation floor
- Maturity envelope
- Authority rules
- Expansion test
- Reassessment

Apply this model to the initiative being changed. Do not inherit maturity from unrelated parts of a repository or organization.

Define the initiative as the requested change plus every current product path, durable record, consumer, and operational contract it can mutate or invalidate. A new mechanism inside a mature data path does not reset the affected initiative to exploratory. An unrelated mature subsystem does not raise it.

## Evidence Dimensions

Assess each dimension from current code, runtime wiring, tests, operations, and user evidence:

- product proof
- consumer evidence
- semantic stability
- operational exposure
- observed failure evidence
- persistence stakes
- integration depth

Do not use design volume, test volume, implementation sophistication, or agent confidence as maturity evidence.

## Posture And Obligation Floor

Use the least mature critical dimension to limit solution breadth. Separately record the highest current consequence that must be preserved as the obligation floor. Durable data, real consumers, security exposure, and service commitments can impose a high obligation floor even when a new mechanism is unproven.

### Exploratory

Use when end-to-end behavior is unproven or core semantics remain unsettled.

- prefer one narrow path through existing modules
- allow characterization tests, local adapters, and reversible experiments
- require approval for new crates, durable stores, generalized protocols, speculative migrations, and compatibility systems
- default to one implementor and one bounded review lane

### First Slice

Use when one narrow end-to-end path works but consumers and contracts remain unstable.

- extend the proven path through existing architecture
- add only durability required by current data and runtime behavior
- require approval for new crates, stores, cross-domain protocols, and generalized public abstractions
- extract shared behavior only from observed duplication or an unavoidable active boundary

### Repeated Use

Use when multiple real paths expose recurring duplication, failure, or stable shared semantics.

- allow bounded shared modules and migrations supported by observed consumers
- require evidence for generalized contracts and background coordination
- design recovery against observed persistence and operational obligations
- retain explicit tripwires for new services, crates, and protocols

### Operational

Use when real users, durable data, upgrades, security exposure, or service obligations require hardening.

- allow recovery, compatibility, observability, and security mechanisms supported by current obligations
- continue to reject speculative generality and unused extension points
- preserve explicit approval gates for major architectural expansion

## Maturity Envelope

Record this envelope before design fan-out or implementation:

```yaml
maturity:
  posture:
  obligation_floor:
  confidence:
  evidence:
  user_override:
  direct_product_proof:
  hard_limits:
    new_crates:
    new_durable_stores:
    new_cross_domain_protocols:
    new_workspace_dependencies:
    parallel_implementors:
  tripwires:
    changed_files:
    added_lines:
  investigation_budget:
    inspection_calls:
    source_files_beyond_named_design_and_policy:
  approval_gates:
  review_budget:
    review_owner:
    reviewer_lanes:
    initial_passes:
    verification_passes:
    reviewer_inspection_calls:
    reviewer_additional_source_files:
```

Default investigation budgets when the user supplies none:

| Posture | Inspection calls | Additional source files |
| --- | ---: | ---: |
| Exploratory | 12 | 16 |
| First Slice | 16 | 24 |
| Repeated Use | 22 | 36 |
| Operational | 28 | 48 |

One inspection call may batch related searches or reads. Do not count required skill and policy reads. Reaching the limit ends discovery and lowers confidence.

Treat hard limits as forbidden without explicit approval. Treat tripwires as mandatory pause points, not coding targets.

Choose provisional tripwires before selecting the implementation shape. Ground them in comparable current slices, active policy, or an explicit user budget. If no evidence-grounded threshold exists, report the estimate as unaccepted and withhold build-ready status.

## Authority Rules

- Make the envelope visible before implementation fan-out.
- Include incumbent obligations used to set the obligation floor.
- Let the user override inferred posture, limits, and gates.
- Pass the accepted envelope verbatim to workers and reviewers.
- Allow simpler approaches and lower maturity findings.
- Forbid workers and reviewers from weakening product proof, raising maturity, relaxing limits, or approving expansion.
- Stop when new evidence contradicts the envelope.

## Expansion Test

Treat each of these as architectural expansion:

- new crate or workspace member
- new durable store or storage backend
- new cross-domain protocol or coordinator
- new background runtime or service
- new public abstraction intended for future consumers
- new compatibility or migration system without current persisted data

Require the proposal to identify the current product behavior that existing architecture cannot deliver. If the envelope does not authorize the expansion, stop before editing and request approval.

## Reassessment

Reassess only from a completed product slice, a new real consumer, an observed failure, or a changed operational obligation. Do not raise maturity because a plan became detailed or an internal subsystem gained tests.
