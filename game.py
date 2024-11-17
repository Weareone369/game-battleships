from grid import Grid 
from player import Player 
import random 

class Game: 
    """Coordinates the overall gameplay between the player and PC opponent."""
    
    def __init__(self, grid_size, player_name): 
        """Set up the game with grids for both player and PC based on grid size.""" 
        self.player_grid = Grid(grid_size) 
        self.pc_grid = Grid(grid_size) 
        self.player = Player(player_name, self.player_grid) 
        self.pc = Player("PC", self.pc_grid) 
        
        # Place ships for player and PC
        self._place_ships(self.player_grid) 
        self._place_ships(self.pc_grid) 
                        
    def start(self): 
        """Main game loop for playing the game."""
        print(f"Hello {self.player.name} get ready to play!")
        print("Your ships are placed. The game begins now!")

        while True:
            # Display boards before each turn
            self.display_boards()

            # Player's turn 
            print("\nTime to attack!")
            self.player.take_turn(self.pc_grid) 
            if not self.pc_grid.ships:
                print(f"Congratulations, {self.player.name}! You sank all PC's ships!")
                break 
                        
            # PC's turn 
            print("PC's turn...") 
            while True: 
                x, y = random.randint(0, self.player_grid.size - 1), random.randint(0, self.player_grid.size - 1) 
                result = self.player_grid.receive_shot(x, y) 
                if result != "already_shot":
                    print(f"PC shot at ({x}, {y}) and it was a {result}!") 
                    break 
                                
                if not self.player_grid.ships:
                    print(f"Game over!, {self.player.name}. The PC sank all your ships!") 
                    break
