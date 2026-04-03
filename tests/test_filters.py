from __future__ import annotations

import numpy as np

from aicartooncam.config import AppConfig
from aicartooncam.filters import apply_style


def test_apply_style_keeps_shape_and_dtype() -> None:
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    cfg = AppConfig()

    for style in ["cartoon", "sketch", "anime", "beauty", "raw"]:
        out = apply_style(frame, style, cfg)
        assert out.shape == frame.shape
        assert out.dtype == frame.dtype
