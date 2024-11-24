import unittest
from unittest.mock import Mock, patch
from src.grid import Grid
from src.player import Player

input_mock_x = Mock()
input_mock_x.return_value = '1'

input_mock_y = Mock()
input_mock_y.return_value = '1'

input_mock = Mock()

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(size=5)
        self.opponent_grid = Grid(size=5)
        self.player = Player(name="TestPlayer", grid=self.grid)

    def test_player_initialization(self):
        """Test player initialization."""
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.grid, self.grid)

    def test_take_turn_hit(self):
        """Test player taking a turn and hitting a ship."""
        input_mock.side_effect = [input_mock_x.return_value, input_mock_y.return_value]
        with patch('builtins.input', input_mock):
            self.opponent_grid.add_ship([(1, 1), (1, 2)])
            result = self.player.take_turn(self.opponent_grid)
            self.assertEqual(result, "hit")

    def test_take_turn_miss(self):
        """Test player taking a turn and missing."""
        input_mock.side_effect = [input_mock_x.return_value, input_mock_y.return_value]
        with patch('builtins.input', input_mock):
            self.opponent_grid.add_ship([(2, 2), (2, 3)])
            result = self.player.take_turn(self.opponent_grid)
            self.assertEqual(result, "miss")

