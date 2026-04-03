from __future__ import annotations

import time
from dataclasses import asdict

import cv2
import numpy as np

from .config import AppConfig
from .filters import apply_style

try:
    import pyvirtualcam
except ImportError:  # pragma: no cover
    pyvirtualcam = None


class CameraPipeline:
    def __init__(self, config: AppConfig) -> None:
        self.config = config

    def _open_capture(self) -> cv2.VideoCapture:
        cap = cv2.VideoCapture(self.config.camera_index)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.config.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.config.height)
        cap.set(cv2.CAP_PROP_FPS, self.config.fps)
        return cap

    def run(self) -> None:
        cap = self._open_capture()
        if not cap.isOpened():
            raise RuntimeError(
                f"Failed to open camera index {self.config.camera_index}. Config: {asdict(self.config)}"
            )

        virtual_cam = None
        if self.config.virtual_cam:
            if pyvirtualcam is None:
                raise RuntimeError(
                    "pyvirtualcam is not installed. Install with: pip install 'ai-cartoon-cam[virtualcam]'"
                )
            virtual_cam = pyvirtualcam.Camera(
                width=self.config.width,
                height=self.config.height,
                fps=self.config.fps,
                fmt=pyvirtualcam.PixelFormat.BGR,
            )
            print(f"[virtualcam] Started device: {virtual_cam.device}")

        last = time.perf_counter()

        try:
            while True:
                ok, frame = cap.read()
                if not ok:
                    print("[warn] Camera read failed, retrying...")
                    continue

                frame = cv2.resize(frame, (self.config.width, self.config.height))
                styled = apply_style(frame, self.config.style, self.config)

                now = time.perf_counter()
                fps = 1.0 / max(1e-6, now - last)
                last = now
                cv2.putText(
                    styled,
                    f"Style={self.config.style} FPS={fps:.1f}",
                    (16, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (30, 255, 30),
                    2,
                    cv2.LINE_AA,
                )

                if self.config.preview:
                    cv2.imshow("ai-cartoon-cam", styled)

                if virtual_cam is not None:
                    virtual_cam.send(styled)
                    virtual_cam.sleep_until_next_frame()

                key = cv2.waitKey(1) & 0xFF
                if key in (27, ord("q")):
                    break

        finally:
            cap.release()
            cv2.destroyAllWindows()
            if virtual_cam is not None:
                virtual_cam.close()
