# Roborock Local Server (house fork)

The upstream add-on, built on this machine from the `house` branch of
https://github.com/Chrisrkilv/local_roborock_server instead of pulling the published image.
It is upstream `main` plus two add-on options that are offered upstream as separate changes:

- `timezone`: the IANA time zone the server gives the vacuum from its location endpoint,
  for example `Europe/London`. Blank uses the region's default (`Europe/Berlin` for `eu`).
- `tls_domains`: with `tls_mode: cloudflare_acme`, the certificate covers `stack_fqdn` plus
  these exact names instead of `tls_base_domain` and its wildcard. `tls_base_domain` may then
  be blank.

Log rotation (`log_max_size_mb`, `log_backup_count`) is upstream's own, from `main`.
Runtime logs and traces are left out of Home Assistant backups.

Everything else is the same as the upstream add-on; see its documentation in
`roborock_local_server_addon/DOCS.md`.

## Updating

1. Merge the wanted branches into `house` and push.
2. Set `SOURCE_REF` in `Dockerfile` to that commit, bump `version` in `config.yaml`, add a
   line to `CHANGELOG.md`, commit and push.
3. In Home Assistant, check for updates in the add-on store and update; it rebuilds.
