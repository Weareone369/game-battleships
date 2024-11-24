class Grid:
    """Handles grid setup, display, and
    interactions for the Battleships game."""

    def __init__(self, size):
        """Initialize the grid with a given size and empty cells."""
        self.size = size
        self.ships = []
        self.grid = [['~' for _ in range(size)] for _ in range(size)]

    def add_ship(self, ship):
        """Add a ship to the grid if placement is valid.
        A ship is defined as a list of (x, y) tuples
        representing its coordinates."""
        for x, y in ship:
            if not (0 <= x < self.size and 0 <= y < self.size):
                raise ValueError("Ship is out of bounds.")
            if self.grid[x][y] != '~':
                raise ValueError("Ship overlaps with another ship.")

        self.ships.append(ship)
        for x, y in ship:
            self.grid[x][y] = 'S'

    def receive_shot(self, x, y):
        """Process a shot at coordinates (x, y).
        Returns 'hit', 'miss', or 'sink' based on target location."""
        if not (0 <= x < self.size and 0 <= y < self.size):
            raise ValueError("Shot is out of bounds.")

        if self.grid[x][y] == 'S':
            self.grid[x][y] = 'X'  # Mark as hit
            for ship in self.ships:
                if (x, y) in ship:
                    ship.remove((x, y))
                if not ship:
                    self.ships.remove(ship)
                    return "sink"
                return "hit"
        elif self.grid[x][y] == '~':
            self.grid[x][y] = 'O'  # Mark as miss
            return "miss"
        else:
            return "already_shot"

    def display(self, reveal=False):
        """Display the grid, Reveal ship's if 'reveal' is True."""
        for row in self.grid:
            print(" ".join(cell if reveal or cell not in ['S'] else '~' for cell in row))
