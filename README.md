# Battleships Game 

Welcome to Battleships, a classic turn-based strategy game where you sink the enemy fleet before they sink yours! This Python-based implementation allows a single player to challenge an PC opponent in a fun and interactive battle. 

## Features

- A customizable grid size for more challenging games. 
- A visual display of both the player’s board and the PC’s board (ships hidden).
- Intelligent AI that randomly places ships and takes shots. 
- Interactive turn-based gameplay with clear feedback for hits, misses, and sinks. 
- Graceful error handling for invalid or out-of-bound inputs. 
- Clean, modular code for easy maintenance and testing. 

## Gameplay Overview 

1. **Objective**:
   - Destroy all of your opponent’s ships before they destroy yours. 
2. **Setup**:
   - The game randomly places ships on a grid for both the player and the PC.
   - Ships are of varying lengths (e.g., 2 or 3 cells). 
3. **Turns**:
   - The player takes turns firing shots at the AI’s grid. 
   - The AI responds by firing back at the player’s grid. 
   - Feedback for each shot indicates whether it was a hit, miss, or sunk ship. 
4. **Win Condition**:
   - The first player to sink all of the opponent’s ships wins the game. 

## How to Run the Game 

### Prerequisites 

- Python 3.8 or later installed on your system. 

### Setup 

1. Clone the repository:
   
`git clone https://github.com/yourusername/battleships_game.git cd battleships_game`

2. Run the game:
   
`python main.py`

## Folder Structure 
<img width="480" alt="Screenshot 2024-11-21 at 18 23 24" src="https://github.com/user-attachments/assets/97b1bef8-2e8f-4997-9be6-e66cefb7ced0">

## How to Play 

1. Launch the game by running main.py.
2. Enter your name when prompted. 
3. View your grid and begin firing shots by entering row and column coordinates.
   - Example: Enter row: 2 and Enter column: 3.
4. The game will display feedback for hits, misses, and sunk ships. 
5. Continue playing until all ships on either grid are destroyed. 

## Game Screenshots

### Initializing game
<img width="427" alt="Screenshot 2024-11-21 at 18 16 32" src="https://github.com/user-attachments/assets/dcebf818-7a54-47f0-838e-16a19ad7a252">

### Display the first board after firing the first shot
<img width="426" alt="Screenshot 2024-11-21 at 18 17 42" src="https://github.com/user-attachments/assets/158b3997-6dcb-4f15-8470-94b99ce23130">

### Error display when trying to add an incorrect coordinate
<img width="352" alt="Screenshot 2024-11-21 at 18 18 45" src="https://github.com/user-attachments/assets/14c207b6-add9-4251-a077-fe4b34ddbb36">

### Board after firing a few shots
<img width="279" alt="Screenshot 2024-11-21 at 18 18 56" src="https://github.com/user-attachments/assets/4df0b6b3-a972-483b-bb51-66d4525d330d">

## Testing 

Unit tests are available in the tests/ directory for key components such as: 

- **Grid**: Validates ship placement and shot handling.
- **Player**: Tests player actions, including turns and feedback.
- **Game**: Ensures game flow and win/lose conditions are met. 

### Run Tests:

`python -m unittest discover -s tests`

### Output:

You should see output indicating the tests passed:

<img width="570" alt="image" src="https://github.com/user-attachments/assets/af58ce5a-e7a6-41b1-9b33-20bdc628469b">

## Future Improvements 

- Add support for additional ship types and sizes.
- Allow manual placement of ships by the player.
- Add a difficulty level for the PC opponent.
- Implement a graphical user interface (GUI). 
