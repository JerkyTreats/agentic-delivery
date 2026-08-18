# Phase Packets

Use packets to constrain one active product slice. Do not pass the whole roadmap as implementation authority.

## Worker Packet

Include:

- accepted maturity envelope verbatim
- direct product behavior and proof
- active slice scope
- frozen affected-domain set when applicable
- existing seams to reuse
- explicit non-goals
- hard limits and tripwires
- approval gates and approved expansions
- owned write scope
- permitted read scope
- forbidden changes
- selected tests and gates
- commit expectation
- parent review owner
- branch or worktree

Require the worker to stop before unapproved expansion or after a tripwire breach. Require direct product evidence and a complexity delta in the final report.

## Review Packet

Include:

- maturity envelope
- direct product proof
- active slice only
- integrated diff or commit range
- complexity delta
- expansion decisions
- gate evidence
- current policy
- frozen review budget
- initial or verification marker

For an initial pass, ask for active-path correctness, maturity fit, and unnecessary architecture. Freeze returned findings.

For verification, pass only accepted finding identifiers and the fix diff. Permit only verification of those findings and regressions caused by their fixes.

## Blocking Standard

A finding blocks only for:

- failed direct acceptance evidence
- incorrect active-path behavior
- concrete current data or security risk
- applicable policy violation
- maturity-envelope violation

Defer future scaling, planned consumers, speculative durability, and generalized hardening.

## Fix Packet

Include:

- accepted finding identifiers
- maturity envelope
- exact fix scope
- files owned
- forbidden expansion
- regression evidence
- gates to rerun
- verification ownership
- commit expectation

Do not let a fix worker reinterpret the objective or add adjacent improvements.
