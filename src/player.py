class Player:
    """Represents a player in the game, managing their grid and shots."""

    def __init__(self, name, grid):
        """Initialize player with a name and their own grid."""
        self.name = name
        self.grid = grid

    def take_turn(self, opponent_grid):
        """ Allow player to take a turn by choosing a shot
        at opponent's grid. Returns feedback for hit or miss."""
        while True:
            try:
                print(f"{self.name}, it's your turn!")
                x = int(input("Enter row: "))
                y = int(input("Enter column: "))
                result = opponent_grid.receive_shot(x, y)
                if result == "already_shot":
                    print("You already shot here! Try again.")

                else:
                    print(f"{self.name}'s shot: {result}")
                    return result

            except ValueError as e:
                print(f"Invalid input: {e}. Try again.")
