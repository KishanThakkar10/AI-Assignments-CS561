# Tic-Tac-Toe Game with Alpha-Beta Pruning

This Python script implements a Tic-Tac-Toe game with a graphical user interface (GUI) using Tkinter library. The AI opponent in this game is optimized with the alpha-beta pruning algorithm for efficient decision-making.

## Features

1. **Graphical User Interface (GUI):** Utilizes Tkinter for creating a user-friendly interface.
2. **Player vs. AI:** Allows the player to play against an AI opponent that makes moves using the alpha-beta pruning algorithm.
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

### Alpha-Beta Pruning Algorithm

- Enhances the minimax algorithm with alpha-beta pruning for efficient pruning of search trees.
- Optimizes AI decision-making by reducing unnecessary exploration of subtrees.

## Usage

1. **Running the Script:** Execute the script using Python (`python script_name.py`).
2. **Gameplay:** Click on the buttons to make moves. Play against the AI opponent.
3. **Game Result:** After the game ends, a dialog box displays the result (win, draw).
4. **Exit:** Close the window or press the close button on the result dialog.

## Dependencies

- Python 3.x
- Tkinter library (standard in Python)


