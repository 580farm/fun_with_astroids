from dataclasses import dataclass


@dataclass(frozen=True)
class GameSettings:
    title: str = "Fun with Asteroids"
    width: int = 960
    height: int = 640
    fps: int = 60
    round_seconds: int = 45
    asteroid_count: int = 6
    ship_radius: int = 16
    ship_x: int = 170
    vertical_thrust: float = 980.0
    vertical_damping: float = 0.97
    max_vertical_speed: float = 420.0
    asteroid_speed: float = 230.0
    completion_bonus: int = 1000
    survival_bonus_per_second: int = 12
    asteroid_dodge_bonus: int = 75
    collision_penalty: int = 150
    credit_divisor: int = 100


SETTINGS = GameSettings()

SPACE = (8, 12, 24)
STAR = (235, 238, 245)
SHIP = (116, 214, 255)
SHIP_THRUST = (255, 205, 112)
ASTEROID = (166, 154, 136)
ASTEROID_OUTLINE = (98, 90, 82)
TEXT = (235, 238, 245)
WARNING = (255, 125, 125)
