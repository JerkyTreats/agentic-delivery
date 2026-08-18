# AGENTS.md

## Public Repository Privacy Boundary

Treat this repository and its history as public.

Do not copy, infer, or publish user-specific topology from the working environment. This includes:

- absolute home or workspace paths
- personal account names or machine names
- private hostnames, domains, addresses, ports, or service URLs
- local network, cluster, storage, deployment, or service-discovery layout
- private repository names, infrastructure names, connector configuration, or account identifiers
- credentials, tokens, secrets, or identifying fragments derived from them

This boundary applies to source files, documentation, examples, fixtures, tests, snapshots, logs, generated artifacts, commit messages, pull requests, issues, and review comments.

Use neutral placeholders such as `<user-home>`, `<workspace>`, `<internal-host>`, `<private-service>`, and `<account>` whenever an example needs environmental context. Keep examples minimal and describe only the portable contract or behavior.

Do not treat information visible on the local filesystem, in environment variables, in command output, or through connected tools as suitable for publication. Access does not imply publication authority.

Before committing or publishing, inspect the complete change for topology and identifying details. If a task genuinely requires private environmental data, keep that data outside this repository and document only the abstract interface. Stop and ask the user before publishing any uncertain identifier.
