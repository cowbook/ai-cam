from __future__ import annotations

import cv2
import numpy as np

from .config import AppConfig


def _odd(n: int) -> int:
    return n if n % 2 == 1 else n + 1


def cartoon_filter(frame: np.ndarray, cfg: AppConfig) -> np.ndarray:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, _odd(cfg.edge_blur_ksize))

    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        _odd(cfg.edge_block_size),
        3,
    )

    color = frame.copy()
    for _ in range(max(1, cfg.bilateral_passes)):
        color = cv2.bilateralFilter(
            color,
            d=cfg.bilateral_d,
            sigmaColor=cfg.bilateral_sigma_color,
            sigmaSpace=cfg.bilateral_sigma_space,
        )

    return cv2.bitwise_and(color, color, mask=edges)


def sketch_filter(frame: np.ndarray, _: AppConfig) -> np.ndarray:
    gray, color = cv2.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    _ = gray
    return color


def anime_filter(frame: np.ndarray, cfg: AppConfig) -> np.ndarray:
    stylized = cv2.stylization(
        frame,
        sigma_s=cfg.stylization_sigma_s,
        sigma_r=cfg.stylization_sigma_r,
    )
    return cartoon_filter(stylized, cfg)


def beauty_filter(frame: np.ndarray, cfg: AppConfig) -> np.ndarray:
    smooth = frame.copy()
    for _ in range(max(1, cfg.beauty_passes)):
        smooth = cv2.bilateralFilter(
            smooth,
            d=cfg.beauty_d,
            sigmaColor=cfg.beauty_sigma_color,
            sigmaSpace=cfg.beauty_sigma_space,
        )

    # Blend in a little detail to keep facial features from looking too plastic.
    detail = cv2.addWeighted(frame, 1.35, cv2.GaussianBlur(frame, (0, 0), 2.0), -0.35, 0)
    merged = cv2.addWeighted(smooth, 0.82, detail, 0.18, 0)
    adjusted = cv2.convertScaleAbs(merged, alpha=cfg.beauty_contrast, beta=cfg.beauty_brightness)

    hsv = cv2.cvtColor(adjusted, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[..., 1] = np.clip(hsv[..., 1] * cfg.beauty_saturation, 0, 255)
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)


def apply_style(frame: np.ndarray, style: str, cfg: AppConfig) -> np.ndarray:
    mode = style.lower()
    if mode == "cartoon":
        return cartoon_filter(frame, cfg)
    if mode == "sketch":
        return sketch_filter(frame, cfg)
    if mode == "anime":
        return anime_filter(frame, cfg)
    if mode == "beauty":
        return beauty_filter(frame, cfg)
    if mode == "raw":
        return frame
    raise ValueError(f"Unknown style '{style}'. Use: cartoon, sketch, anime, beauty, raw")
