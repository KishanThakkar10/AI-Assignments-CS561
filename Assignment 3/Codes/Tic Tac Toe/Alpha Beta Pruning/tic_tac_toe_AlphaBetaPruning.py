import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    # Define color attributes as class attributes
    x_color = "pink"
    o_color = "blue"
    draw_color = "red"
    x_win_color = "green"
    o_win_color = "green"

    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 30), width=4, height=2, bg='black', fg=TicTacToeGUI.x_color,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)


    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.current_player == 'X':
                self.buttons[row][col].config(fg=self.x_color)
            else:
                self.buttons[row][col].config(fg=self.o_color)
            result = self.check_win()
            if result:
                self.show_result(result)
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'O':
                    self.ai_move()

    def ai_move(self):
        _, best_move = self.alphabeta(0, True, float('-inf'), float('inf'))
        row, col = best_move
        self.board[row][col] = 'O'
        self.buttons[row][col].config(text='O', fg=self.o_color)
        result = self.check_win()
        if result:
            self.show_result(result)
        else:
            self.current_player = 'X'

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        # Check for draw
        if all(self.board[row][col] != ' ' for row in range(3) for col in range(3)):
            return 'Draw'

        # Game still ongoing
        return None

    def alphabeta(self, depth, maximizing_player, alpha, beta):
        result = self.check_win()
        if result is not None:
            if result == 'X':
                return -10 + depth, None
            elif result == 'O':
                return 10 - depth, None
            else:
                return 0, None

        if maximizing_player:
            best_score = -float('inf')
            best_move = None
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'O'
                        score, _ = self.alphabeta(depth + 1, False, alpha, beta)
                        self.board[row][col] = ' '  # Undo the move
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'X'
                        score, _ = self.alphabeta(depth + 1, True, alpha, beta)
                        self.board[row][col] = ' '  # Undo the move
                        if score < best_score:
                            best_score = score
                            best_move = (row, col)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score, best_move

    def show_result(self, result):
        if result == 'Draw':
            for row in self.buttons:
                for button in row:
                    button.config(fg=self.draw_color)
            messagebox.showinfo("Game Result", "It's a Draw!")
        elif result == 'X':
            for row in self.buttons:
                for button in row:
                    if button.cget("text") == 'X':
                        button.config(fg=self.x_win_color)
                    else:
                        button.config(fg=self.o_color)
            messagebox.showinfo("Game Result", "Player X wins!")
        elif result == 'O':
            for row in self.buttons:
                for button in row:
                    if button.cget("text") == 'O':
                        button.config(fg=self.o_win_color)
                    else:
                        button.config(fg=self.x_color)
            messagebox.showinfo("Game Result", "Player O wins!")
            
        self.root.after(1000, lambda: self.root.destroy())


def main():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
