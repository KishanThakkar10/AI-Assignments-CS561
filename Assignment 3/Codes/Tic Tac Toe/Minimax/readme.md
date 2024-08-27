# Tic-Tac-Toe Game with Adversarial Search (Minimax)

This Python script implements a simple Tic-Tac-Toe game using the Tkinter library for GUI and the minimax algorithm for an AI opponent. Below is an overview of the code and its functionalities.

## Features

1. **Graphical User Interface (GUI):** Utilizes Tkinter for creating a user-friendly interface.
2. **Player vs. AI:** Allows the player to play against an AI opponent that makes moves using the minimax algorithm.
3. **Win Detection:** Detects wins, draws, or ongoing game state.
4. **Colorful Display:** Visual cues for X, O, draw, and winning moves.
5. **Game Result Dialog:** Displays a dialog box showing the game result.

## Components

### `TicTacToeGUI` Class

- Manages the game logic and GUI elements.
- Initializes the game board, players, colors, and buttons.
- Contains methods for handling player clicks, AI moves, win detection, and displaying game results.

### `main()` Function

- Entry point of the script.
- Creates the Tkinter window and initializes the game instance.

### Minimax Algorithm

- Implements the minimax algorithm for AI decision-making.
- Recursively evaluates possible moves and selects the best move for the AI opponent.

## Usage

1. **Running the Script:** Execute the script using Python (`python script_name.py`).
2. **Gameplay:** Click on the buttons to make moves. Play against the AI opponent.
3. **Game Result:** After the game ends, a dialog box displays the result (win, draw).
4. **Exit:** Close the window or press the close button on the result dialog.

## Dependencies

- Python 3.x
- Tkinter library (standard in Python)

## Enhancements

- Implement alpha-beta pruning for optimizing the minimax algorithm.

