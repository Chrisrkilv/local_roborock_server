import re
import tomllib
from pathlib import Path

import yaml

from roborock_local_server import __version__


def test_package_version_matches_pyproject() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    assert pyproject["project"]["version"] == __version__


def test_init_module_exports_single_version_literal() -> None:
    init_text = Path("src/roborock_local_server/__init__.py").read_text(encoding="utf-8")
    matches = re.findall(r'__version__\s*=\s*"([^"]+)"', init_text)
    assert matches == [__version__]


def test_home_assistant_addon_version_matches_package_version() -> None:
    # The house add-on is built from this branch: the package version plus a house build number.
    addon = yaml.safe_load(Path("roborock_local_server_house_addon/config.yaml").read_text(encoding="utf-8"))
    assert re.fullmatch(rf"{re.escape(__version__)}-house[0-9.]+", addon["version"])


def test_addon_turn_defaults_to_disabled_without_reserving_udp_ports() -> None:
    addon = yaml.safe_load(Path("roborock_local_server_house_addon/config.yaml").read_text(encoding="utf-8"))
    assert addon["schema"]["turn_mode"] == "list(disabled|provided|external)?"
    assert addon["options"]["turn_mode"] == "disabled"
    assert addon["ports"]["3478/udp"] is None
    assert all(addon["ports"][f"{port}/udp"] is None for port in range(49160, 49180))
