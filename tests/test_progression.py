import unittest

from fun_with_asteroids.progression import STARTER_SPACECRAFT, STARTER_UPGRADES


class ProgressionTests(unittest.TestCase):
    def test_starter_spacecraft_have_required_fields(self):
        for spacecraft in STARTER_SPACECRAFT:
            self.assertTrue(spacecraft.name)
            self.assertTrue(spacecraft.program)
            self.assertTrue(spacecraft.era)
            self.assertTrue(spacecraft.handling)

    def test_starter_upgrades_cover_each_tree(self):
        trees = {upgrade.tree for upgrade in STARTER_UPGRADES}
        self.assertEqual(trees, {"Pilot", "Engineer", "Navigator"})


if __name__ == "__main__":
    unittest.main()
