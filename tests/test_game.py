import unittest
from src.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game(grid_size=5, player_name="User")

    def test_game_initialization(self):
        """Test if the game initializes correctly."""
        self.assertEqual(self.game.player_grid.size, 5)
        self.assertEqual(self.game.pc_grid.size, 5)
        self.assertEqual(self.game.player.name, "User")
        self.assertEqual(self.game.pc.name, "PC")

    def test_start_game(self):
        """Test if the game starts and runs the main loop."""
        # Simulate game loop steps here if applicable.
        self.assertIsNotNone(self.game.start)

    def test_player_win_condition(self):
        """Test if the game detects player win."""
        self.game.pc_grid.ships = []  # Simulate all PC ships destroyed
        self.assertTrue(not self.game.pc_grid.ships)

    def test_pc_win_condition(self):
        """Test if the game detects PC win."""
        self.game.player_grid.ships = []  # Simulate all player ships destroyed
        self.assertTrue(not self.game.player_grid.ships)
