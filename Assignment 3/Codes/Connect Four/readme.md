# Connect Four Game with Adversarial Search

This Python script implements a Connect Four game with a graphical user interface (GUI) using the Tkinter library. The AI opponent in this game uses the minimax algorithm with alpha-beta pruning for efficient decision-making.

## Features

1. **Graphical User Interface (GUI):** Utilizes Tkinter for creating a user-friendly interface.
2. **Player vs. AI:** Allows the player to play against an AI opponent that makes moves using the minimax algorithm.
3. **Win Detection:** Detects wins, draws, or ongoing game state.
4. **Colorful Display:** Visual representation of pieces (red for human player, yellow for AI player).
5. **Game Result Display:** Shows a message indicating the game result (win, lose, or tie).

## Components

### `Board` Class

- Represents the game board and manages game state.
- Provides methods for dropping pieces, checking validity of moves, checking for wins, and evaluating the board.

### `Minimax` Class

- Implements the minimax algorithm with alpha-beta pruning for AI decision-making.
- Calculates the best move for the AI opponent.

### `ConnectFourGUI` Class

- Manages the game GUI and interaction with the user.
- Creates the game window, handles player clicks, and displays game results.

### `main()` Function

- Entry point of the script.
- Initializes the Tkinter window and the Connect Four game instance.

## Usage

1. **Running the Script:** Execute the script using Python (`python script_name.py`).
2. **Gameplay:** Click on the columns to drop pieces. Play against the AI opponent.
3. **Game Result:** After the game ends, a message displays the result (win, lose, or tie).
4. **Exit:** Close the window to exit the game.

## Dependencies

- Python 3.x
- Tkinter library (standard in Python)

