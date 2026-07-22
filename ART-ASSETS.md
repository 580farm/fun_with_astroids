# Art Assets

## Art Direction

The game should read clearly at arcade speed while still hinting at real
spacecraft history. Early assets can be simple silhouettes. Later art can add
panel lines, antennas, heat shields, solar panels, and country-specific visual
details.

## Visual Priorities

1. Player spacecraft must be instantly recognizable.
2. Asteroids must be easy to see against space.
3. Pickups must look different from hazards.
4. UI text must stay readable.
5. Historical details should support gameplay rather than clutter it.

## Starter Placeholder Assets

The first implementation uses Pygame drawing commands:

- A triangular capsule-style player ship.
- Circular asteroids with outline rings.
- Text HUD for time, score, hits, and credits.
- Solid-color space background.

These placeholders are acceptable until core gameplay feels good.

## Sprite Targets

Recommended sprite sizes:

- Small spacecraft: 32x32 or 48x48
- Large spacecraft: 64x64
- Small asteroid: 24x24
- Medium asteroid: 40x40
- Large asteroid: 64x64
- UI icons: 16x16 or 24x24

Keep sprites readable when rotated and scaled.

## Spacecraft Visual Notes

- Mercury: compact cone capsule with small retro pack.
- Vostok: spherical descent module with service module hints.
- Gemini: cone capsule, slightly larger and sharper than Mercury.
- Apollo CSM: command module plus service module shape.
- Soyuz: orbital module, descent module, service module, and solar panels.
- Space Shuttle: winged orbiter silhouette.
- Buran: similar winged orbiter, visually distinguished by markings.
- Dragon: blunt capsule with trunk or solar panel hints for cargo variants.
- Orion: larger modern capsule silhouette.
- Starliner: rounded capsule with service module.
- New Shepard: crew capsule style with booster represented in museum art.
- Starship: large stainless launch vehicle, likely a special late unlock.

## Sound Direction

Sound should be playful and not too intense:

- Soft thrust loop.
- Short collision thump.
- Pickup chime.
- Level complete flourish.
- Menu select blip.
- Low warning tone when time is almost out.

## Asset Folder Plan

Future assets should live under:

```text
assets/
├── fonts/
├── images/
│   ├── spacecraft/
│   ├── asteroids/
│   ├── pickups/
│   └── ui/
└── sounds/
```

Assets are not required for the first scaffold.
