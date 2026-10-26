# Changelog

## 1.2.1-house4

- First build from the fork: upstream `main` at 206d560 (after 1.2.1, with built-in log
  rotation and the TURN relay) plus `addon-timezone-option` and `addon-acme-exact-names`.
- Replaces the local add-on that wrapped the 1.2.1 image. `tls_exact_names` and
  `tls_extra_names` become one list, `tls_domains`; `stack_fqdn` is always included.
