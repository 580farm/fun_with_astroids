# Fun with Asteroids - Game Design Document

## Vision

Fun with Asteroids is a family-built fixed 2D side-scroller inspired by simple
dodge games. Players fly historically accurate spacecraft from the
Space Race through today, avoiding asteroid fields instead of destroying them.

The project is also a hands-on way to learn Python programming together. Each
new feature should connect a visible game result to a programming idea: game
loops, movement, sprites, collisions, score, menus, data files, and simple
object-oriented design.

## Player Fantasy

You are a spacecraft pilot threading a dangerous side-scrolling path through
space history. A tiny Mercury capsule feels different from a Space Shuttle,
Soyuz, Dragon, or Orion. Each ship has tradeoffs, and each country or space
program unlocks its own style of technology.

## Core Gameplay

- Dodge asteroids.
- Stay near the left side of the screen while hazards enter from the right.
- Use vertical thrusters to move up and down in zero gravity.
- Complete timed levels.
- Earn points for surviving, dodging asteroids, collecting helpful powerups, and
  avoiding damage.
- Lose points or credits for asteroid impacts.
- Unlock new spacecraft and upgrades with credits earned from play.
- Explore tech trees that differ by country or space program.

## First Playable Version

The first version should be intentionally small:

- One spacecraft.
- One side-scrolling asteroid lane.
- One timed round.
- Basic score display.
- Collision penalties.
- Restart and quit flow.

This gives the project a complete loop before adding menus, artwork, sound, or
progression.

## Scoring Model

The initial score should be simple enough to explain:

- Start from a level completion bonus.
- Add survival time during the run.
- Add a bonus for each asteroid that passes safely.
- Add bonuses for collected powerups.
- Subtract points for each asteroid hit.
- Convert a portion of score into credits.

The exact numbers can change during playtesting. Early values should favor fun
and encouragement over strict difficulty.

## Progression

Progression is split into three upgrade families:

- Pilot: flight feel and maneuvering.
- Engineer: survival, shielding, and durability.
- Navigator: awareness, prediction, and time-control abilities.

Each family should unlock gradually so the player always has a clear next goal.

## Unlockables

Early spacecraft list:

- Mercury
- Vostok
- Voskhod
- Gemini
- Apollo CSM
- Soyuz, including major generations
- Space Shuttle
- Buran
- ISS cargo vehicles
- Dragon
- Orion
- Starliner
- New Shepard
- Starship, when appropriate for the game's historical scope

Spacecraft should be represented with short museum-style notes in addition to
gameplay stats.

## Educational Goals

- Learn Python fundamentals.
- Learn variables, functions, classes, modules, and packages.
- Learn game loops, events, sprites, movement, collision detection, and timers.
- Learn how version control helps a project grow safely.
- Learn spaceflight history through spacecraft unlocks and in-game notes.

## Tone

The game should feel energetic, curious, and playful. It should treat real
spacecraft with respect while staying approachable for younger players and new
programmers.

## Future Ideas

- Local co-op.
- Endless mode.
- Boss asteroid fields.
- Space museum with facts for every unlocked spacecraft.
- Multiple space programs with different tech trees.
- Historical challenge missions inspired by real eras.
