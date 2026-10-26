# House build of the Roborock Local Server add-on.
# The Supervisor builds this folder on its own, so the server source at the repo root is not
# in the build context. Instead: upstream's 1.2.1 image (same system packages and Python
# dependencies, pinned by digest), with the server package replaced by this fork's house
# branch at SOURCE_REF. Dependencies in pyproject.toml are unchanged since 1.2.1, hence --no-deps.
# To update: merge into house, push, set SOURCE_REF to that commit, bump version in config.yaml.
ARG BUILD_FROM
FROM ghcr.io/python-roborock/local_roborock_server:1.2.1@sha256:0f3d0dd05f14315273df5622d43008b2665c24b2fed79277822d4c9184eab158

ARG SOURCE_REF=3b12317589fe8d75d649af6ae5bd2cea7043cd7d

# coturn joined upstream's Dockerfile after 1.2.1 (provided TURN mode).
RUN apt-get update \
  && apt-get install -y --no-install-recommends coturn \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --no-deps --force-reinstall \
    "https://github.com/Chrisrkilv/local_roborock_server/archive/${SOURCE_REF}.tar.gz" \
  && python -c "from roborock_local_server.ha_addon import DEFAULT_OPTIONS; assert 'timezone' in DEFAULT_OPTIONS and 'tls_domains' in DEFAULT_OPTIONS"
