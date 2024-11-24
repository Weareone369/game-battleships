import unittest
from src.grid import Grid


class TestGrid(unittest.TestCase):
    def setUp(self): self.grid = Grid(size=5)

    def test_initial_grid_setup(self):
        """Test if the grid is initialized correctly."""
        self.assertEqual(len(self.grid.grid), 5)
        self.assertTrue(all(len(row) == 5 for row in self.grid.grid))

    def test_add_ship_valid(self):
        """Test adding a valid ship to the grid."""
        result = self.grid.add_ship([(1, 1), (1, 2), (1, 3)])
        self.assertEqual([[(1, 1), (1, 2), (1, 3)]], self.grid.ships)

    def test_add_ship_invalid(self):
        """Test adding a ship out of bounds."""
        with self.assertRaises(ValueError):
            self.grid.add_ship([(6, 6), (6, 7)])

    def test_receive_shot_hit(self):
        """Test receiving a shot that hits a ship."""
        self.grid.add_ship([(2, 2), (2, 3)])
        result = self.grid.receive_shot(2, 2)
        self.assertEqual(result, "hit")

    def test_receive_shot_miss(self):
        """Test receiving a shot that misses."""
        self.grid.add_ship([(2, 2), (2, 3)])
        result = self.grid.receive_shot(0, 0)
        self.assertEqual(result, "miss")

    def test_receive_shot_sink(self):
        """Test sinking a ship."""
        self.grid.add_ship([(3, 3)])
        result = self.grid.receive_shot(3, 3)
        self.assertEqual(result, "sink")
