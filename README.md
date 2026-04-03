# ai-cartoon-cam

[![CI](https://github.com/cowbook/ai-cam/actions/workflows/ci.yml/badge.svg)](https://github.com/cowbook/ai-cam/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/cowbook/ai-cam?sort=semver)](https://github.com/cowbook/ai-cam/releases)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform: macOS](https://img.shields.io/badge/platform-macOS-black?logo=apple)](https://www.apple.com/macos/)

A local real-time camera stylization project for macOS, designed for OBS and livestream workflows.

## Quick Start

### 1) Clone and enter project

```bash
git clone git@github.com:cowbook/ai-cam.git
cd ai-cam
```

### 2) Create environment and install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[virtualcam,dev]'
```

### 3) Run real-time preview

```bash
ai-cartoon-cam --style cartoon
```

Try another style:

```bash
ai-cartoon-cam --style beauty
```

### 4) Run with config

```bash
ai-cartoon-cam --config examples/config.sample.yaml
```

### 5) Output to virtual camera for OBS

```bash
ai-cartoon-cam --style beauty --virtual-cam
```

Then in OBS, select the pyvirtualcam device as your camera source.

## Vision

Build an open-source, continuously improving project for:

- Real-time cartoon/sketch/anime style effects.
- Smooth macOS local inference and camera processing.
- OBS virtual camera output for livestreaming platforms.
- A plugin-friendly architecture for future AI models.

## Current features (v0.1.0)

- Real-time webcam capture via OpenCV.
- Built-in styles: cartoon, sketch, anime, beauty, raw.
- Optional virtual camera output via pyvirtualcam.
- YAML config support.
- CLI entrypoint for fast experiments.

## Project structure

```text
ai-cartoon-cam/
  src/aicartooncam/
    cli.py
    config.py
    filters.py
    pipeline.py
  tests/
  examples/
  docs/
```

## Install

```bash
cd /Volumes/T4/2026/ai-cartoon-cam
python -m venv .venv
source .venv/bin/activate
pip install -e '.[virtualcam,dev]'
```

## Run

### Basic preview

```bash
ai-cartoon-cam --style cartoon
```

```bash
ai-cartoon-cam --style beauty
```

### Use config file

```bash
ai-cartoon-cam --config examples/config.sample.yaml
```

### Save and load presets

Save a merged preset (defaults + config + CLI overrides):

```bash
ai-cartoon-cam --config examples/config.sample.yaml --style anime --save-preset stream-anime
```

Load a preset by name on next run:

```bash
ai-cartoon-cam --preset stream-anime
```

By default presets are stored in `~/.ai-cartoon-cam/presets`. You can override with `--preset-dir`.

### Output to OBS virtual camera

```bash
ai-cartoon-cam --style beauty --virtual-cam
```

Then in OBS, choose the virtual camera device produced by pyvirtualcam.

## AI Session Continuity

To continue work across new chats/sessions, start with:

- aiwork/memory.md
- aiwork/continue-prompt.md

Update `aiwork/memory.md` after every meaningful change so later sessions can resume quickly.

## Inspired by GitHub projects

This project borrows architecture and practical ideas from the open-source ecosystem:

- OpenCV image stylization and filtering pipelines:
  - https://github.com/opencv/opencv
- Real-time segmentation and media processing design:
  - https://github.com/google-ai-edge/mediapipe
- OBS plugin and streaming workflow patterns:
  - https://github.com/obsproject/obs-studio
- Community camera style transfer experiments:
  - https://github.com/topics/style-transfer

No code is copied from these repositories. References are used for learning design patterns and best practices.

## Roadmap

- Add face-aware skin smoothing with landmark protection.
- Add temporal stabilization to reduce frame flicker.
- Add ONNX Runtime backend for model-based stylization.
- Add preset manager and hotkey switching.
- Add benchmark mode for FPS/latency profiling.

## License

MIT
