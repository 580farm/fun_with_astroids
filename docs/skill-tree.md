# Skill Tree

The upgrade system should make each replay feel useful without overwhelming a
new player. The first version can store these as simple data. Later versions can
draw them as actual branching trees.

## Pilot Tree

Focus: movement skill and ship handling.

| Upgrade | Effect | Notes |
| --- | --- | --- |
| Quick Climb | Increases vertical thrust | Helps dodge tight asteroid gaps |
| Boost | Adds a short burst upward or forward | Should have a cooldown |
| Better Handling | Reduces vertical floatiness | Makes capsules easier for beginners |
| Precision Thrusters | Improves small altitude changes | Good for docking-style levels |
| Evasive Roll | Briefly reduces collision penalty | Could be a late upgrade |

## Engineer Tree

Focus: survival and ship systems.

| Upgrade | Effect | Notes |
| --- | --- | --- |
| Shield | Absorbs one collision | Clear visual feedback needed |
| Hull Reinforcement | Reduces collision penalty | Good early safety upgrade |
| Reduced Cooldowns | Recharges abilities faster | Helps all play styles |
| Emergency Repair | Restores one hit during a level | Should be limited |
| System Redundancy | Keeps controls stable after damage | Useful in hard levels |

## Navigator Tree

Focus: awareness, planning, and timing.

| Upgrade | Effect | Notes |
| --- | --- | --- |
| Trajectory Prediction | Shows short asteroid paths | Teaches vectors visually |
| Radar | Highlights incoming right-side hazards | Useful when speeds increase |
| Slow Motion | Briefly slows hazards | Strong ability, use a cooldown |
| Route Planner | Adds bonus path markers | Could support challenge levels |
| Sensor Boost | Increases pickup detection range | Good non-combat reward |

## Unlock Rules

- First upgrade in each tree should be cheap.
- Later upgrades should require previous upgrades in the same tree.
- The player should be able to mix trees.
- Credits should come from playing, not from perfection only.

## First Implementation

Start with three upgrades:

- Quick Climb
- Shield
- Radar

These map clearly to player movement, collision handling, and awareness.
