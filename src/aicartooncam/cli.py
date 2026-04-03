from __future__ import annotations

import argparse

from .config import AppConfig, load_config, load_preset, save_preset
from .pipeline import CameraPipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local real-time cartoon camera pipeline")
    parser.add_argument("--config", type=str, default=None, help="Path to yaml config")
    parser.add_argument("--preset", type=str, default=None, help="Load a named preset (yaml under preset dir)")
    parser.add_argument("--preset-dir", type=str, default=None, help="Override preset directory")
    parser.add_argument("--save-preset", type=str, default=None, help="Save merged config as a named preset and exit")
    parser.add_argument("--camera-index", type=int, default=None)
    parser.add_argument("--width", type=int, default=None)
    parser.add_argument("--height", type=int, default=None)
    parser.add_argument("--fps", type=int, default=None)
    parser.add_argument("--style", type=str, default=None, choices=["cartoon", "sketch", "anime", "beauty", "raw"])
    parser.add_argument("--virtual-cam", action="store_true", help="Enable virtual camera output")
    parser.add_argument("--no-preview", action="store_true", help="Disable local preview window")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    config = load_config(args.config)
    preset_config = load_preset(args.preset, args.preset_dir) if args.preset else AppConfig()

    override = {
        "camera_index": args.camera_index,
        "width": args.width,
        "height": args.height,
        "fps": args.fps,
        "style": args.style,
        "virtual_cam": True if args.virtual_cam else None,
        "preview": False if args.no_preview else None,
    }

    final_config = AppConfig().merge(config.__dict__).merge(preset_config.__dict__).merge(override)

    if args.save_preset:
        path = save_preset(args.save_preset, final_config, args.preset_dir)
        print(f"[preset] Saved: {path}")
        return

    CameraPipeline(final_config).run()


if __name__ == "__main__":
    main()
