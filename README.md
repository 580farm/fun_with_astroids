# Fun with Asteroids

A family-built 2D arcade game about flying real spacecraft through asteroid
fields. The first goal is a small, playable Python game. The bigger goal is to
learn programming, game design, and spaceflight history together.

Players dodge asteroids instead of destroying them. Levels are timed, scores
reward careful flying, and credits unlock historical spacecraft, pilot skills,
engineering upgrades, and navigation tools.

## Current Status

This repo is at the starter scaffold stage:

- Project documentation is organized from the initial design notes.
- A minimal Pygame CE game loop is in place.
- The player ship can turn, thrust, drift, wrap around the screen, and collide
  with moving asteroids.
- A small test suite covers early data structures and scoring behavior.

## Quick Start

Requirements:

- Python 3.11 or newer
- Git

Create a virtual environment and install the project:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Run the game:

```bash
python -m fun_with_asteroids
```

Run tests:

```bash
python -m unittest
```

## Controls

- `Left` / `A`: rotate counterclockwise
- `Right` / `D`: rotate clockwise
- `Up` / `W`: thrust
- `Escape`: quit

## Project Map

- [GAME-DESIGN.md](GAME-DESIGN.md): vision, gameplay, progression, and scope
- [TECHNICAL-SPEC.md](TECHNICAL-SPEC.md): architecture and implementation notes
- [ROADMAP.md](ROADMAP.md): milestone plan and task list
- [ART-ASSETS.md](ART-ASSETS.md): visual, sound, and UI asset direction
- [SPACECRAFT.md](SPACECRAFT.md): historical spacecraft reference
- [IDEAS.md](IDEAS.md): brainstorms and future features
- [docs/skill-tree.md](docs/skill-tree.md): pilot, engineer, and navigator upgrades
- [docs/gameplay-loop.md](docs/gameplay-loop.md): moment-to-moment play flow
- [docs/educational-notes.md](docs/educational-notes.md): programming and history goals

## Design Pillars

1. **Dodge, do not destroy.** The game is about skillful flight through danger.
2. **Real spacecraft first.** Ships should be inspired by actual vehicle shapes,
   eras, countries, and mission roles.
3. **Small playable steps.** Every milestone should teach one useful concept and
   leave the game more fun than before.
4. **Family-friendly challenge.** The game should be readable, forgiving at
   first, and rewarding as players improve.
