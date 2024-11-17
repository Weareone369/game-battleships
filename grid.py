class Grid: 
    """Handles grid setup, display, and interactions for the Battleships game.""" 
    
    def __init__(self, size): 
        """Initialize the grid with a given size and empty cells.""" 
        self.size = size 
        self.ships = [] 
        self.grid = [['~' for _ in range(size)] for _ in range(size)] 

    def display(self, reveal=False):
        """Display the grid, Reveal ship's if 'reveal' is True."""
        for row in self.grid:
            print(" ".join(cell if reveal or cell not in ['S'] else '~' for cell in row))
