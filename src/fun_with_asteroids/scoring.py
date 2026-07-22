from dataclasses import dataclass

from .config import SETTINGS, GameSettings


@dataclass(frozen=True)
class ScoreBreakdown:
    completion_bonus: int
    survival_bonus: int
    dodge_bonus: int
    powerup_bonus: int
    collision_penalty: int

    @property
    def total(self) -> int:
        return max(
            0,
            self.completion_bonus
            + self.survival_bonus
            + self.dodge_bonus
            + self.powerup_bonus
            - self.collision_penalty,
        )


def calculate_score(
    seconds_survived: float,
    collisions: int,
    asteroids_dodged: int = 0,
    powerup_bonus: int = 0,
    settings: GameSettings = SETTINGS,
) -> ScoreBreakdown:
    safe_seconds = max(0, int(seconds_survived))
    safe_collisions = max(0, collisions)
    safe_dodges = max(0, asteroids_dodged)
    safe_powerups = max(0, powerup_bonus)

    return ScoreBreakdown(
        completion_bonus=settings.completion_bonus,
        survival_bonus=safe_seconds * settings.survival_bonus_per_second,
        dodge_bonus=safe_dodges * settings.asteroid_dodge_bonus,
        powerup_bonus=safe_powerups,
        collision_penalty=safe_collisions * settings.collision_penalty,
    )


def credits_from_score(score: int, settings: GameSettings = SETTINGS) -> int:
    return max(0, score) // settings.credit_divisor
