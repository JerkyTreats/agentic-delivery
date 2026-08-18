---
name: assessment-by-domain
description: Run a breadth-first assessment across a system's complete domain landscape, then decompose only the affected domains one level. Use when a concern may cross three or more ownership boundaries, isolated analysis could miss integrations, ownership is unclear, or planning needs an evidence-backed impact map before implementation.
---

# Assessment By Domain

## Purpose

Expose cross-domain interaction without centralizing domain authority or turning every traversed domain into implementation scope.

Use two bounded passes:

1. sweep the complete current domain set
2. decompose each affected domain one level

Stop after synthesis. Do not turn the assessment into an implementation plan unless the caller explicitly requests the next operation.

## Establish The Domain Universe

Derive domains from current evidence rather than from a proposed solution. Depending on the system, domains may be product capabilities, services, packages, data owners, teams, lifecycle areas, or independently governed operational surfaces.

Record the evidence used to define the domain universe. Include every current top-level domain once, including explicit `none` results. Do not add hypothetical consumers or planned subsystems.

## Define The Concern

Record:

- concern in one paragraph
- direct behavior being assessed
- explicit in-scope behavior
- explicit out-of-scope behavior
- current evidence basis
- applicable policy or authority
- any caller-supplied limits or maturity envelope

Begin with the behavior whose ownership must be traced, not with a proposed subsystem.

Preserve caller-supplied limits verbatim. The assessment may expose a required decision or recommend a smaller affected set. It may not relax limits, approve expansion, or raise maturity.

Set a discovery budget before inspecting beyond user-named sources and policy. Default to 12 batched inspection calls and 20 additional source items when the caller supplies no budget. Count searches, file reads, history queries, and diagnostics. Reaching the limit ends discovery and lowers confidence. It does not authorize another pass.

## Pass One: Domain Sweep

Assess every domain before decomposing any one domain.

| Domain | Needed integration | Current integration | Completeness | Evidence | Non-integration rationale | Follow-up |
| --- | --- | --- | --- | --- | --- | --- |

Use these integration levels:

- `none` for no truthful direct relationship
- `observe` for diagnostics or read-only visibility
- `publish` for domain-owned output consumed by the concern
- `consume` for concern input used by domain behavior
- `own` for source truth or behavior owned by the domain
- `adapter` for parsing, mapping, routing, or presentation only

Use these completeness values:

- `not needed`
- `not started`
- `partial`
- `complete`
- `blocked`

Evidence must cite current code, tests, runtime behavior, operational records, authoritative policy, or another current source. Planned behavior is not current integration.

Freeze the affected-domain set after this pass. It contains every row whose needed integration is not `none`.

## Pass Two: Affected-Domain Decomposition

For each affected domain, identify one level of major internal concerns from its public contracts, current organization, and direct role in the behavior.

Prefer behavioral names such as query, admission, realization, persistence, publication, assembly, authorization, or observation. Do not manufacture generic technical layers or enumerate every file.

| Domain concern | Owner | Current ground | Required relationship | Change posture | Boundary risk | Evidence |
| --- | --- | --- | --- | --- | --- | --- |

Use these change postures:

- `reuse unchanged`
- `extend existing`
- `new local behavior`
- `adapter only`
- `not needed`

Name the smallest existing seam that can carry each required relationship. Treat a new cross-domain contract as a finding, not an automatic recommendation.

Do not recurse into a third level unless the user requests it or current evidence reveals another independently owned boundary. File and function discovery belongs to later implementation planning.

## Delegate Without Losing Breadth

Use subagents only when the caller or active environment permits delegation and the domain sets can be inspected independently.

Keep one synthesis owner. Give every worker the same concern, scope, evidence standard, caller limits, and output columns. Assign complete domain batches and require explicit `none` rows. Do not ask workers to design the intended architecture.

Freeze the affected set centrally after all pass-one batches return. During pass two, workers may refine evidence inside that set. A newly discovered domain boundary returns to the synthesis owner for one bounded update rather than silently expanding scope.

## Synthesize

Extract:

- concern owners
- domains that publish or consume contracts
- adapters that only map or route
- domains reused unchanged
- explicit non-integration decisions
- cross-domain boundary risks
- smallest missing connective behavior
- unresolved ownership questions
- exact affected-domain set

Separate these scopes:

1. domains on the runtime or operating path
2. domains whose behavior must change
3. implementation units likely to change

Never promote the first set into the third.

## Stop Conditions

Stop after the second pass and synthesis.

Re-run only when the concern changes, a new domain appears, an ownership boundary moves, or implementation evidence invalidates the frozen affected set.

Do not create workstreams, implementation sequencing, acceptance tests, migration steps, or generalized infrastructure unless the caller requests that next operation.

## Required Output

Produce one assessment containing:

- concern and scope
- regenerated domain snapshot
- pass-one domain sweep
- frozen affected-domain set
- pass-two affected-domain decomposition
- ownership and boundary synthesis
- separated runtime, behavior-change, and write scopes
- explicit non-integration decisions
- evidence basis and confidence
- unresolved questions
