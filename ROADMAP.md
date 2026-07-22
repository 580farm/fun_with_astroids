# Roadmap

## Milestone 0: Project Foundation

Status: started

- Organize design documentation.
- Add Python package scaffolding.
- Add dependency metadata.
- Add a runnable game entry point.
- Add first tests.

## Milestone 1: First Window

Goal: open a game window and close it cleanly.

- Initialize Pygame CE.
- Create a fixed-size window.
- Draw a background.
- Handle quit and Escape key events.
- Show a simple title in the window caption.

## Milestone 2: Player Ship

Goal: make one spacecraft feel good to fly.

- Draw the starter ship.
- Rotate left and right.
- Thrust forward.
- Add drift and drag.
- Wrap around screen edges.

## Milestone 3: Asteroid Field

Goal: create the first real obstacle.

- Spawn asteroids at different positions.
- Give asteroids different sizes and speeds.
- Wrap asteroids around screen edges.
- Avoid unfair spawning directly on top of the player.

## Milestone 4: Collisions and Feedback

Goal: make danger understandable.

- Detect ship and asteroid collisions.
- Add hit cooldown so one collision does not count many times.
- Flash or tint the ship after a hit.
- Add a simple hit counter.

## Milestone 5: Scoring

Goal: make each run measurable.

- Add countdown timer.
- Add score calculation.
- Add credits earned.
- Show a level complete screen.
- Track a local high score.

## Milestone 6: Menus and Restart Flow

Goal: make the game feel complete.

- Add start menu.
- Add pause state.
- Add game over and level complete screens.
- Add restart without closing the program.

## Milestone 7: Upgrades

Goal: give players reasons to replay.

- Add pilot, engineer, and navigator skill trees.
- Add basic credit spending.
- Apply upgrades to ship handling, shields, and radar.
- Save unlock progress locally.

## Milestone 8: Historical Spacecraft

Goal: make the game's history theme visible.

- Add spacecraft stats.
- Add spacecraft selection.
- Add museum facts.
- Add historically inspired silhouettes or sprites.
- Add country or program tech trees.

## Milestone 9: Polish

Goal: make the game satisfying to share.

- Add sound effects.
- Add music.
- Add sprite animation.
- Add particle effects.
- Tune difficulty.
- Package a playable build.

## Backlog

- Local co-op.
- Endless mode.
- Boss asteroid fields.
- Challenge missions.
- Accessibility options.
- Controller support.
