# Agentic Delivery

Agentic Delivery packages two reusable agent skills for architectural analysis and long-horizon engineering work.

- `assessment-by-domain` sweeps the complete domain landscape before decomposing affected domains.
- `delivery-program` turns broad intent into an authorized program and delivers one evidence-backed slice at a time.

The skills are repository-agnostic. They read and preserve the active host, repository, and user policies rather than embedding one project's governance.

## Install For Every Codex Session

Clone the repository, then link its skills into the user skill catalog:

```bash
git clone https://github.com/JerkyTreats/agentic-delivery.git
cd agentic-delivery
python3 scripts/install.py --target codex
```

Codex discovers user skills from `~/.agents/skills`. It loads skill metadata at startup and loads full instructions only when a request matches or the skill is explicitly invoked.

Restart Codex if a newly installed skill does not appear.

## Install For Other Agents

The repository follows the open agent skills layout. The installer includes adapters for user skill roots already used by several local agents:

```bash
python3 scripts/install.py --target claude
python3 scripts/install.py --target pi
```

Install into any other compatible skill root with:

```bash
python3 scripts/install.py --root /path/to/user/skills
```

The installer creates links back to the checkout so a normal `git pull` updates every linked agent. It refuses to replace existing paths.

## Use

Invoke either skill explicitly:

```text
$assessment-by-domain assess this proposed change before we plan it
$delivery-program design a program for this long-horizon objective
$delivery-program deliver the next authorized slice
```

Automatic matching remains enabled for both skills. The delivery skill still requires explicit implementation authorization before it edits, commits, or advances beyond an accepted boundary.

## Plugin Packaging

The repository is also a skills-only Codex plugin. Its manifest lives at `.codex-plugin/plugin.json`, and both bundled skills live under `skills/`.

This makes the same source suitable for local marketplaces and future publication through the shared plugin directory without changing the skill packages.

## Validate

Run the repository checks with:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

The checks validate plugin metadata, skill frontmatter, UI metadata, relative links, helper behavior, and unfinished scaffold markers.

## Design Boundaries

Assessment produces an impact map and stops. It does not create an implementation program unless requested.

Delivery owns program design and authorized implementation. It treats roadmap detail as context, keeps one active slice, and pauses at architectural expansion or scope gates.

Neither skill requires a hosted service, private infrastructure, or external connector.

## License

Licensed under Apache License 2.0. See `LICENSE`.
