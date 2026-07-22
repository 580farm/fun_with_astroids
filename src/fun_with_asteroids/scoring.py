from dataclasses import dataclass

from .config import SETTINGS, GameSettings


@dataclass(frozen=True)
class ScoreBreakdown:
    completion_bonus: int
    time_bonus: int
    powerup_bonus: int
    collision_penalty: int

    @property
    def total(self) -> int:
        return max(
            0,
            self.completion_bonus
            + self.time_bonus
            + self.powerup_bonus
            - self.collision_penalty,
        )


def calculate_score(
    seconds_remaining: float,
    collisions: int,
    powerup_bonus: int = 0,
    settings: GameSettings = SETTINGS,
) -> ScoreBreakdown:
    safe_seconds = max(0, int(seconds_remaining))
    safe_collisions = max(0, collisions)
    safe_powerups = max(0, powerup_bonus)

    return ScoreBreakdown(
        completion_bonus=settings.completion_bonus,
        time_bonus=safe_seconds * settings.time_bonus_per_second,
        powerup_bonus=safe_powerups,
        collision_penalty=safe_collisions * settings.collision_penalty,
    )


def credits_from_score(score: int, settings: GameSettings = SETTINGS) -> int:
    return max(0, score) // settings.credit_divisor
