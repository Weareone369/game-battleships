#Battleships Game 

Welcome to Battleships, a classic turn-based strategy game where you sink the enemy fleet before they sink yours! This Python-based implementation allows a single player to challenge an PC opponent in a fun and interactive battle. 

Features

• A customizable grid size for more challenging games. 

• A visual display of both the player’s board and the PC’s board (ships hidden). • Intelligent AI that randomly places ships and takes shots. 

• Interactive turn-based gameplay with clear feedback for hits, misses, and sinks. 

• Graceful error handling for invalid or out-of-bound inputs. 

• Clean, modular code for easy maintenance and testing. 

Gameplay Overview 

1. Objective: Destroy all of your opponent’s ships before they destroy yours. 

2. Setup: • The game randomly places ships on a grid for both the player and the AI. • Ships are of varying lengths (e.g., 2 or 3 cells). 

3. Turns: • The player takes turns firing shots at the AI’s grid. 

• The AI responds by firing back at the player’s grid. 

• Feedback for each shot indicates whether it was a hit, miss, or sunk ship. 

4. Win Condition: The first player to sink all of the opponent’s ships wins the game. 

How to Run the Game 

Prerequisites 

• Python 3.8 or later installed on your system. 

Setup 

1. Clone the repository: 

git clone https://github.com/yourusername/battleships_game.git cd battleships_game 

2. Install dependencies (if any are listed in requirements.txt): 

pip install -r requirements.txt 

3. Run the game: 

python main.py 

Folder Structure 

battleships_game/ 
├── README.md                      # Project documentation 
├── requirements.txt               # External 
libraries needed for the project 
── main.py                         # Main entry point to run the game 
├── src/                           # Source code for the game 
│ 
├── __init__.py                    # Marks src/ as a package 
│ ├── game.py                      # Game logic and main game loop 
│ ├── grid.py                      # Grid class handling grid setup and shots 
│ └── player.py                    # Player class handling user and AI players 
├── tests/                         # Test files for the project 
│ ├── __init__.py                  # Marks tests/ as a package 
│ ├── test_game.py                 # Tests for Game class 
│ ├── test_grid.py                 # Tests for Grid class 
│ └── test_player.py               # Tests for Player class 

How to Play 

1. Launch the game by running main.py. 

2. Enter your name when prompted. 

3. View your grid and begin firing shots by entering row and column coordinates. 

• Example: Enter row: 2 and Enter column: 3. 

4. The game will display feedback for hits, misses, and sunk ships. 

5. Continue playing until all ships on either grid are destroyed. 

Example Gameplay Welcome to Battleships! 
Enter your name: Alex 
Hello Alex, get ready to play! 

Alex's Board:
~ ~ ~ ~ ~
~ ~ ~ ~ ~ 
~ ~ S S S 
~ ~ ~ ~ ~ 
~ ~ S S ~ 

PC's Board (hidden):
~ ~ ~ ~ ~
~ ~ ~ ~ ~ 
~ ~ ~ ~ ~ 
~ ~ ~ ~ ~ 
~ ~ ~ ~ ~ 

Your turn! 
Enter row (0-indexed): 2 
Enter column (0-indexed): 4 
Your shot: hit 

PC's turn... 
PC shot at (3, 1) and it was a miss! 

Testing 

Unit tests are available in the tests/ directory for key components such as: 

• Grid: Validates ship placement and shot handling. 

• Player: Tests player actions, including turns and feedback. 

• Game: Ensures game flow and win/lose conditions are met. 

To run the tests: 

python -m unittest discover -s tests 

Future Improvements 

• Add support for additional ship types and sizes. 

• Allow manual placement of ships by the player. 

• Add a difficulty level for the PC opponent. 

• Implement a graphical user interface (GUI). 




