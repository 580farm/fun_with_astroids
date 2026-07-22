# Gameplay Loop

## Core Loop

1. Choose or continue with a spacecraft.
2. Start a timed asteroid field.
3. Dodge asteroids while managing speed and direction.
4. Collect optional powerups.
5. Finish the timer.
6. Receive score and credits.
7. Spend credits on spacecraft, skills, or upgrades.
8. Try a harder level or improve the previous score.

## Moment-to-Moment Feel

The ship should feel like it is floating in space:

- Thrust adds momentum.
- Turning changes facing direction.
- Releasing thrust should not stop the ship immediately.
- A little drag keeps the game manageable.
- Wrapping around the screen keeps movement continuous.

## Round Structure

Recommended starter round:

- Duration: 60 seconds
- Asteroids: 6
- Ship: Mercury-style starter capsule
- Collision penalty: 150 points
- Completion bonus: 1000 points
- Time bonus: 10 points per second remaining

## Failure and Success

The game should avoid harsh failure in the earliest versions. Instead of losing
immediately, collisions subtract score and may reduce end-of-round credits.
Harder modes can add limited hull or lives later.

## HUD

The first HUD should show:

- Time remaining
- Score
- Hits
- Credits preview

Later HUD additions:

- Shield status
- Ability cooldowns
- Radar indicator
- Current spacecraft
- Level name

## Difficulty Tuning

Difficulty can increase through:

- More asteroids.
- Faster asteroid speeds.
- Larger asteroid sizes.
- Longer rounds.
- Fewer powerups.
- Narrower safe paths.

Difficulty should be changed one variable at a time during playtesting so the
family can tell what made the round easier or harder.
