# Contributing

Thank you for contributing to ai-cartoon-cam.

## Development setup

1. Create and activate a Python 3.10+ virtual environment.
2. Install dependencies:

```bash
pip install -e '.[dev,virtualcam]'
```

3. Run tests:

```bash
pytest
```

## Pull request checklist

- Keep changes scoped and well described.
- Add tests for behavior changes.
- Run lint and tests before opening a PR.
- Update README if user-facing behavior changed.

## Coding style

- Follow PEP 8.
- Prefer small pure functions for image filters.
- Keep camera loop resilient to temporary frame read failures.
