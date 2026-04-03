from __future__ import annotations

from dataclasses import asdict

from aicartooncam.config import AppConfig, load_preset, save_preset


def test_save_and_load_preset_roundtrip(tmp_path) -> None:
    cfg = AppConfig(style="anime", width=960, height=540, fps=24, virtual_cam=True)

    saved_path = save_preset("streaming", cfg, preset_dir=str(tmp_path))
    assert saved_path.exists()

    loaded = load_preset("streaming", preset_dir=str(tmp_path))
    assert asdict(loaded) == asdict(cfg)


def test_load_preset_supports_yaml_suffix(tmp_path) -> None:
    cfg = AppConfig(style="sketch")
    save_preset("quick.yaml", cfg, preset_dir=str(tmp_path))

    loaded = load_preset("quick.yaml", preset_dir=str(tmp_path))
    assert loaded.style == "sketch"
