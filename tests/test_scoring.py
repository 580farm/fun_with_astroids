import unittest

from fun_with_asteroids.config import GameSettings
from fun_with_asteroids.scoring import calculate_score, credits_from_score


class ScoringTests(unittest.TestCase):
    def test_score_rewards_time_and_penalizes_collisions(self):
        settings = GameSettings(
            completion_bonus=1000,
            time_bonus_per_second=10,
            collision_penalty=150,
        )

        score = calculate_score(
            seconds_remaining=12,
            collisions=2,
            powerup_bonus=50,
            settings=settings,
        )

        self.assertEqual(score.total, 870)

    def test_score_never_goes_below_zero(self):
        score = calculate_score(seconds_remaining=0, collisions=100)
        self.assertEqual(score.total, 0)

    def test_credits_use_score_divisor(self):
        settings = GameSettings(credit_divisor=100)
        self.assertEqual(credits_from_score(870, settings), 8)


if __name__ == "__main__":
    unittest.main()
