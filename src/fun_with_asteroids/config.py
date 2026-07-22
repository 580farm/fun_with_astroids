from dataclasses import dataclass


@dataclass(frozen=True)
class GameSettings:
    title: str = "Fun with Asteroids"
    width: int = 960
    height: int = 640
    fps: int = 60
    round_seconds: int = 60
    asteroid_count: int = 7
    ship_radius: int = 16
    completion_bonus: int = 1000
    time_bonus_per_second: int = 10
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
