import tkinter as tk
import math
import random

# Constants
EMPTY = 0
HUMAN_PLAYER = 1
AI_PLAYER = 2

# Board dimensions
ROWS = 6
COLUMNS = 7

class Board:
    def __init__(self):
        self.board = [[EMPTY] * COLUMNS for _ in range(ROWS)]

    def drop_piece(self, column, piece):
        for i in range(ROWS - 1, -1, -1):
            if self.board[i][column] == EMPTY:
                self.board[i][column] = piece
                return i, column
        return None, None

    def is_valid_move(self, column):
        return self.board[0][column] == EMPTY

    def get_valid_columns(self):
        return [col for col in range(COLUMNS) if self.is_valid_move(col)]

    def is_full(self):
        return all(self.board[0])

    def won_game(self, piece):
        for i in range(ROWS):
            for j in range(COLUMNS - 3):
                if self.board[i][j] == piece and \
                   self.board[i][j + 1] == piece and \
                   self.board[i][j + 2] == piece and \
                   self.board[i][j + 3] == piece:
                    return True
        for i in range(ROWS - 3):
            for j in range(COLUMNS):
                if self.board[i][j] == piece and \
                   self.board[i + 1][j] == piece and \
                   self.board[i + 2][j] == piece and \
                   self.board[i + 3][j] == piece:
                    return True
        for i in range(ROWS - 3):
            for j in range(COLUMNS - 3):
                if self.board[i][j] == piece and \
                   self.board[i + 1][j + 1] == piece and \
                   self.board[i + 2][j + 2] == piece and \
                   self.board[i + 3][j + 3] == piece:
                    return True
        for i in range(3, ROWS):
            for j in range(COLUMNS - 3):
                if self.board[i][j] == piece and \
                   self.board[i - 1][j + 1] == piece and \
                   self.board[i - 2][j + 2] == piece and \
                   self.board[i - 3][j + 3] == piece:
                    return True
        return False

class Minimax:
    def __init__(self):
        self.max_depth = 4

    def find_move(self, board):
        return self.minimax(board, self.max_depth, True)[0]

    def minimax(self, board, depth, maximizing_player):
        if depth == 0 or board.won_game(HUMAN_PLAYER) or board.won_game(AI_PLAYER) or board.is_full():
            return None, self.evaluate_board(board)

        valid_columns = board.get_valid_columns()

        if maximizing_player:
            max_eval = -math.inf
            best_move = random.choice(valid_columns)
            for col in valid_columns:
                row, _ = board.drop_piece(col, AI_PLAYER)
                _, eval = self.minimax(board, depth - 1, False)
                board.board[row][col] = EMPTY
                if eval > max_eval:
                    max_eval = eval
                    best_move = col
            return best_move, max_eval
        else:
            min_eval = math.inf
            best_move = random.choice(valid_columns)
            for col in valid_columns:
                row, _ = board.drop_piece(col, HUMAN_PLAYER)
                _, eval = self.minimax(board, depth - 1, True)
                board.board[row][col] = EMPTY
                if eval < min_eval:
                    min_eval = eval
                    best_move = col
            return best_move, min_eval

    def evaluate_board(self, board):
        ai_score = self.get_score(board, AI_PLAYER)
        human_score = self.get_score(board, HUMAN_PLAYER)
        return ai_score - human_score

    def get_score(self, board, piece):
        score = 0
        for i in range(ROWS):
            for j in range(COLUMNS):
                if board.board[i][j] == piece:
                    score += self.get_score_direction(board, i, j, piece)
        return score

    def get_score_direction(self, board, row, col, piece):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        score = 0
        for dr, dc in directions:
            count = 0
            r, c = row, col
            for _ in range(4):
                if 0 <= r < ROWS and 0 <= c < COLUMNS and board.board[r][c] == piece:
                    count += 1
                    r += dr
                    c += dc
                else:
                    break
            if count == 4:
                score += 1000
            elif count == 3:
                score += 100
            elif count == 2:
                score += 10
            elif count == 1:
                score += 1
        return score

class ConnectFourGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Connect Four")
        self.board = Board()
        self.minimax = Minimax()
        self.human_turn = True
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=COLUMNS * 100, height=(ROWS + 1) * 100, bg="#059DFA")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.handle_click)

        self.draw_board()


    def draw_board(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                color = "white"
                if self.board.board[row][col] == HUMAN_PLAYER:
                    color = "red"
                elif self.board.board[row][col] == AI_PLAYER:
                    color = "yellow"
                self.canvas.create_oval(col * 100 + 10, (row + 1) * 100 + 10,
                                        col * 100 + 90, (row + 1) * 100 + 90,
                                        fill=color)

    def handle_click(self, event):
        if not self.human_turn:
            return
        column = event.x // 100
        if self.board.is_valid_move(column):
            row, col = self.board.drop_piece(column, HUMAN_PLAYER)
            self.draw_board()
            if self.board.won_game(HUMAN_PLAYER):
                self.show_message("You win!")
            elif self.board.is_full():
                self.show_message("It's a tie!")
            else:
                self.human_turn = False
                self.ai_move()

    def ai_move(self):
        column = self.minimax.find_move(self.board)
        row, col = self.board.drop_piece(column, AI_PLAYER)
        self.draw_board()
        if self.board.won_game(AI_PLAYER):
            self.show_message("You lose!")
        elif self.board.is_full():
            self.show_message("It's a tie!")
        else:
            self.human_turn = True

    def show_message(self, message):
        self.canvas.create_text(COLUMNS * 50, (0 + 0.5) * 100,
                                text=message, font=("Arial", 20), fill="black")


def main():
    root = tk.Tk()
    game = ConnectFourGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
