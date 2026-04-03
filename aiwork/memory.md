# AI Work Memory (ai-cartoon-cam)

Last updated: 2026-03-28

## 1) Project goal

Build a long-term open-source macOS local real-time camera stylization project for livestreaming workflows (OBS/Bilibili), focused on cartoon/sketch/anime effects and virtual camera output.

## 2) What has been completed

- Project scaffold created under /Volumes/T4/2026/ai-cartoon-cam
- Packaging: pyproject.toml, requirements.txt, installable CLI entry
- Core modules implemented:
  - src/aicartooncam/config.py
  - src/aicartooncam/filters.py
  - src/aicartooncam/pipeline.py
  - src/aicartooncam/cli.py
- Features:
  - Camera capture (OpenCV)
  - Styles: cartoon, sketch, anime, raw
  - Optional virtual camera output (pyvirtualcam)
  - YAML config support
- Open-source basics:
  - LICENSE (MIT)
  - CONTRIBUTING.md
  - CODE_OF_CONDUCT.md
  - GitHub CI workflow and issue templates
- Validation:
  - compileall passed
  - pytest passed (1 test)

## 3) Current environment notes

- A local venv exists in this project: .venv/
- Recommended run path:
  - cd /Volumes/T4/2026/ai-cartoon-cam
  - source .venv/bin/activate
  - ai-cartoon-cam --style cartoon

## 4) Next priorities

1. Face-aware smoothing/masking to avoid over-blurring eyes and mouth.
2. Temporal stabilization to reduce flicker across frames.
3. Preset manager + runtime hotkey/quick switching.
4. ONNX Runtime backend for model-based style transfer.
5. More tests (integration tests for config + style pipeline behavior).

## 5) Decisions and constraints

- Keep everything local-first on macOS.
- Avoid unsafe or identity-deceptive features.
- Design for maintainable open-source iteration.

## 6) Session log template (append below)

- Date:
- What changed:
- Why:
- Validation:
- Next step:

## 7) Session log

- Date: 2026-03-28
- What changed: Added CLI preset manager basics (load/save named YAML presets), introduced `--preset`, `--preset-dir`, `--save-preset`, added config preset helpers, expanded README with preset usage, and added tests in `tests/test_config.py`.
- Why: Roadmap v0.2.0 includes command-line preset save/load and this enables quick repeatable style setup for streaming workflows.
- Validation: `python -m pytest -q` passed (3 tests).
- Next step: Add camera auto-reconnect strategy and pipeline integration tests.

- Date: 2026-03-29
- What changed: Added a new real-time style `beauty` with smoothing + mild detail preservation + brightness/contrast/saturation tuning, wired into CLI choices, added sample config knobs, and updated README usage.
- Why: User requested a beauty-effect mode for livestream camera output.
- Validation: `./.venv/bin/python -m pytest -q` passed (3 tests), and CLI help shows `--style {cartoon,sketch,anime,beauty,raw}`.
- Next step: Optionally add face-aware beauty mask to avoid over-processing eyes/lips.

- Date: 2026-04-03
- What changed: Initialized git repository, prepared first commit, and created/pushed GitHub repository named ai-cam.
- Why: User requested publishing current project to GitHub under repository name ai-cam.
- Validation: Local commit created and remote push to origin completed.
- Next step: Continue feature iteration and open issues/milestones based on roadmap.
