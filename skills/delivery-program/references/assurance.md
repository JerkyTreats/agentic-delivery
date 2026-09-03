# Assurance

Judge one exact candidate in three ordered passes. The passes answer different questions but may record their evidence in one active-slice record.

## Logical Review

Determine whether the candidate implements the frozen slice correctly.

Assess:

- direct product behavior through the real entrypoint
- policy obligations and authorization
- semantic ownership and domain boundaries
- every responsibility disposition
- caller migration and source retirement for `replace` and `move`
- compatibility evidence and write confinement
- scope, maturity, limits, and unnecessary architecture
- persistence, replay, recovery, and identity where applicable

Freeze ordinary findings after one initial pass. The program owner disposes them. Permit one bounded correction and verification by default.

## Style Assurance

Run after logical review over the unchanged exact candidate.

Assess changed-surface comments, domain placement, public boundaries, adapter thinness, formatting, lint, and risk-proportionate tests. Require replay, restart, property, state-machine, or fuzz evidence only where the changed contract exposes corresponding risk or repository precedent.

Style Assurance cannot redesign behavior or move ownership. A discovered logical defect returns to logical review and invalidates the prior style eligibility.

Use `satisfied`, `not satisfied`, or `not eligible`.

## Gate Acceptance

Run after logical review and Style Assurance succeed. Judge whether declared deliverables compose across the frozen coherence horizon.

For each criterion record the claim, producer-consumer edges, acceptable evidence, forbidden substitutions, verdict, and exception authority.

Gate Acceptance does not repair code, waive criteria, amend the slice, authorize commit, or authorize the next slice.

Use `accepted`, `rejected`, or `not eligible`.

## Corrections

For a failed pass, record the finding, owner disposition, exact correction scope, forbidden expansion, evidence to rerun, and stop condition in the active-slice record.

If code changes, create a successor candidate. Rerun the earliest affected pass and every dependent later pass. Verification remains bounded to disposed findings and correction-caused regressions.

## Anomalies

Material evidence that contradicts a frozen or accepted claim is always in scope. Freeze prevents opportunistic scope growth during correction. It does not make a claim immune to falsification.

For an anomaly:

1. record the evidence and affected obligation
2. identify the earliest invalid boundary
3. invalidate dependent verdicts and advancement claims
4. classify it as a design-contract defect, implementation defect, evidence defect, unauthorized scope, or authorized exception
5. return to the authority that owns that boundary
6. create a successor contract or candidate only under explicit authority

Preserve still-valid product evidence. Do not describe a design invalidation as behavioral failure when the behavior remains proved.

## Acceptance Record

Record each pass with candidate identity, evidence, findings, corrections, exceptions, and verdict. Separate files are optional when an independent signature, long-running handoff, or uncommitted candidate manifest needs durable identity.

The final slice outcome must state product acceptance, architectural completeness, commit authority, and next-slice authority separately.
