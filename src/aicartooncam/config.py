from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class AppConfig:
    camera_index: int = 0
    width: int = 1280
    height: int = 720
    fps: int = 30
    style: str = "cartoon"
    preview: bool = True
    virtual_cam: bool = False

    edge_block_size: int = 9
    edge_blur_ksize: int = 7
    bilateral_passes: int = 2
    bilateral_d: int = 9
    bilateral_sigma_color: int = 80
    bilateral_sigma_space: int = 80

    stylization_sigma_s: float = 60.0
    stylization_sigma_r: float = 0.45

    beauty_passes: int = 2
    beauty_d: int = 9
    beauty_sigma_color: int = 50
    beauty_sigma_space: int = 50
    beauty_contrast: float = 1.05
    beauty_brightness: int = 8
    beauty_saturation: float = 1.08

    def merge(self, override: dict[str, Any]) -> "AppConfig":
        data = self.__dict__.copy()
        data.update({k: v for k, v in override.items() if v is not None})
        return AppConfig(**data)


def _resolve_preset_name(name: str) -> str:
    return name if name.endswith((".yaml", ".yml")) else f"{name}.yaml"


def _resolve_preset_dir(preset_dir: str | None) -> Path:
    if preset_dir:
        return Path(preset_dir).expanduser()
    return Path("~/.ai-cartoon-cam/presets").expanduser()


def get_preset_path(name: str, preset_dir: str | None = None) -> Path:
    return _resolve_preset_dir(preset_dir) / _resolve_preset_name(name)


def save_preset(name: str, config: AppConfig, preset_dir: str | None = None) -> Path:
    path = get_preset_path(name, preset_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(asdict(config), f, sort_keys=True)
    return path


def load_preset(name: str, preset_dir: str | None = None) -> AppConfig:
    path = get_preset_path(name, preset_dir)
    if not path.exists():
        raise FileNotFoundError(f"Preset file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    if not isinstance(data, dict):
        raise ValueError("Preset file must contain a mapping object.")

    return AppConfig().merge(data)



def load_config(path: str | None) -> AppConfig:
    if not path:
        return AppConfig()

    cfg_path = Path(path)
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config file not found: {cfg_path}")

    with cfg_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    if not isinstance(data, dict):
        raise ValueError("Config file must contain a mapping object.")

    return AppConfig().merge(data)
