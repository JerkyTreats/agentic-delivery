# Active Slice

The active-slice record begins as the frozen delivery contract and ends as the closeout record for one observable product increment.

## Contract

Record:

- stable slice identifier and baseline
- lifecycle, readiness, and authorization
- observable product behavior and direct proof
- exact in-scope and out-of-scope behavior
- maturity envelope
- frozen affected-domain set
- existing seams to reuse
- owned write scope and permitted read scope
- hard limits, tripwires, and stop conditions
- responsibility disposition table
- candidate evidence and staged judgments
- commit expectation and next authorization boundary

## Responsibility Disposition

Use one row for every changed semantic responsibility.

| Field | Meaning |
| --- | --- |
| responsibility | behavior and semantic owner |
| mode | `new`, `retain`, `extend`, `replace`, or `move` |
| policy obligation | applicable source and requirement |
| current route | runtime entrypoint, real callers, and registration |
| current state | stores, records, recovery, and compatibility |
| successor | intended canonical authority |
| superseded surface | code, exports, writers, adapters, tests, and fuzz targets made obsolete |
| final disposition | retain, delete, or evidence-backed read-only compatibility |
| proof | positive cutover and negative retirement evidence |
| exception | authority, noncanonical route, and removal condition |

For `replace` and `move`, build readiness requires caller migration and retirement within the same completed slice. A later cleanup phase is not a valid disposition.

A compatibility reader must have current stored-data evidence, no semantic writer or selector behavior, an owner, characterization evidence, and a removal condition unless it is an accepted stable contract.

## Policy Trace

Map each applicable policy obligation to its responsibility row, deliverable, proof, and exception authority. Refer to the policy instead of copying it into multiple artifacts.

If local wording narrows an active policy, the slice is not eligible. Route absence cannot substitute for source retirement when policy requires removal.

## Product And Retirement Proof

Define positive proof through the real runtime entrypoint. For replacement work also require negative evidence covering:

- callers and construction sites
- registrations and runtime selection
- public exports and writer APIs
- stores, record families, and recovery
- compatibility paths
- exclusive tests, fixtures, and fuzz targets

Record expected code removal before implementation. After implementation compare actual deletion with the disposition table.

No production deletion or unexpectedly small retirement during replacement triggers an anomaly review. Do not use a fixed addition-to-removal ratio.

## Generated Projections

A worker projection contains only the direct behavior, applicable disposition and policy rows, write scope, reuse seams, non-goals, limits, proof, and stop conditions.

A logical review projection adds the exact candidate, complexity delta, product evidence, and all disposition rows.

A Style Assurance projection adds the logically accepted candidate, changed surface, repository source-quality policy, and relevant test precedent.

A Gate Acceptance projection adds the frozen handoff claims, staged prior verdicts, cross-deliverable evidence, forbidden substitutions, and authorized exceptions.

These projections may be messages or generated text. They are not independent design authorities.

## Closeout

Record the exact candidate, product behavior proved, final responsibility dispositions, removal evidence, retained compatibility, complexity delta, staged verdicts, anomalies, exceptions, commit state, and actions that remain unauthorized.
