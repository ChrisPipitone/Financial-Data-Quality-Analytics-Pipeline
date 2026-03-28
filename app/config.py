from pathlib import Path

import yaml


def load_config(path: str) -> dict:
    config_path = Path(path)
    minimal_configs = ["data-dir"]

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not foound: {path}")

    with config_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError("Config file must contain top-level mapping")

    for config in minimal_configs:
        if config not in data:
            raise ValueError(f"Config file must contain {config}")

    return data
