def main(): 
    """Run the Battleships game."""
    print("Welcome to Battleships!")
    player_name = input("Enter yout name: ")
    game = Game(grid_size = 10, player_name = player_name)
    game.start() 
    
if __name__ == "__main__": 
    main()