# Gameplay Loop

## Core Loop

1. Choose or continue with a spacecraft.
2. Start a timed side-scrolling asteroid lane.
3. Use vertical thrusters to dodge incoming asteroids.
4. Collect optional powerups.
5. Finish the timer.
6. Receive score and credits.
7. Spend credits on spacecraft, skills, or upgrades.
8. Try a harder level or improve the previous score.

## Moment-to-Moment Feel

The ship should feel simple, readable, and slightly floaty:

- The ship stays near the left side of the screen.
- Holding upward thrust moves the ship up.
- Holding downward thrust moves the ship down.
- Releasing controls leaves a little space-like drift that gently settles.
- Asteroids enter from the right and move left.
- Dodging should feel like timing a path through moving gaps.

## Round Structure

Recommended starter round:

- Duration: 45 seconds
- Asteroids: 6
- Ship: Mercury-style starter capsule
- Collision penalty: 150 points
- Completion bonus: 1000 points
- Survival bonus: 12 points per second survived
- Dodge bonus: 75 points per asteroid safely passed

## Failure and Success

The game should avoid harsh failure in the earliest versions. Instead of losing
immediately, collisions subtract score and may reduce end-of-round credits.
Harder modes can add limited hull or lives later.

## HUD

The first HUD should show:

- Time remaining
- Score
- Hits
- Dodged asteroids
- Credits preview

Later HUD additions:

- Shield status
- Ability cooldowns
- Radar indicator
- Current spacecraft
- Level name

## Difficulty Tuning

Difficulty can increase through:

- More asteroids on screen.
- Faster right-to-left asteroid speeds.
- Larger asteroid sizes.
- Longer rounds.
- Fewer powerups.
- Narrower safe paths.

Difficulty should be changed one variable at a time during playtesting so the
family can tell what made the round easier or harder.
