# Technical Specification

## Technology

- Language: Python 3.11+
- Game library: Pygame Community Edition, installed as `pygame-ce`
- Package layout: `src/fun_with_asteroids`
- Test runner: Python's built-in `unittest`
- Version control: Git

## Architecture Goals

The code should stay friendly to new Python learners:

- Prefer small modules with clear names.
- Keep pure game rules separate from Pygame rendering when practical.
- Add comments only where they explain a non-obvious idea.
- Keep configuration values in one place.
- Make every milestone runnable.

## Current Package Layout

```text
src/fun_with_asteroids/
├── __init__.py
├── __main__.py
├── config.py
├── entities.py
├── game.py
├── progression.py
└── scoring.py
```

## Module Responsibilities

- `config.py`: screen size, colors, movement tuning, level timing, and scoring
  constants.
- `entities.py`: player ship and asteroid behavior.
- `game.py`: Pygame initialization, event loop, update, render, and shutdown.
- `progression.py`: starter spacecraft and upgrade tree data.
- `scoring.py`: score and credit calculations.
- `__main__.py`: allows `python -m fun_with_asteroids`.

## Game Loop

Each frame should follow the same rhythm:

1. Read player input and window events.
2. Update the level timer.
3. Update player movement.
4. Update asteroid movement.
5. Check collisions.
6. Update score state.
7. Draw the frame.
8. Wait just enough to maintain the target frame rate.

## Coordinate System

Pygame uses screen coordinates:

- `x` grows from left to right.
- `y` grows from top to bottom.
- `(0, 0)` is the top-left corner.

The first playable version wraps ships and asteroids around screen edges. This
keeps gameplay continuous and avoids immediate failure at the borders.

## Asset Strategy

The starter version uses simple vector-like drawing through Pygame primitives.
This avoids blocking programming progress on art. Later milestones can replace
these shapes with sprite sheets while keeping the same entity behavior.

## Data Strategy

Spacecraft and skill data begin as Python dataclasses. When the lists grow,
they can move to JSON, TOML, or CSV so young contributors can edit content
without touching gameplay code.

## Testing Strategy

Early tests focus on pure functions and structured data:

- Score calculations.
- Credit conversion.
- Upgrade tree integrity.
- Spacecraft data completeness.

Pygame rendering and input should be manually playtested at first. Automated
integration tests can come later if the project grows.

## Setup Commands

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m unittest
python -m fun_with_asteroids
```

## Future Technical Tasks

- Add sprite loading and animation helpers.
- Add menu state management.
- Add save data for unlocks and high scores.
- Add sound effects and music volume controls.
- Add a simple content file format for spacecraft facts.
- Add packaged game builds for sharing with family.
