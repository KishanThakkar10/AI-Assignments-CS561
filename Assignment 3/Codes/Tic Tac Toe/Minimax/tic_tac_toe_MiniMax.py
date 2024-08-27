import tkinter as tk
import random

class SnakeLadderGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake and Ladder Game")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="white")
        self.canvas.pack()
        
        self.board_size = 10
        self.cell_size = 40
        self.player_position = 0
        
        self.draw_board()
        self.draw_player()
        
        self.roll_button = tk.Button(master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()
        
        self.message_label = tk.Label(master, text="")
        self.message_label.pack()
        
        self.snakes_and_ladders = {14: 4, 31: 9, 35: 20, 44: 22, 51: 16, 66: 48, 71: 42, 80: 63}
        
    def draw_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black")
                
    def draw_player(self):
        row = self.player_position // self.board_size
        col = self.player_position % self.board_size
        x0 = col * self.cell_size + 5
        y0 = row * self.cell_size + 5
        x1 = x0 + self.cell_size - 10
        y1 = y0 + self.cell_size - 10
        self.player = self.canvas.create_oval(x0, y0, x1, y1, fill="red")
        
    def move_player(self, steps):
        self.player_position += steps
        if self.player_position in self.snakes_and_ladders:
            self.player_position = self.snakes_and_ladders[self.player_position]
        self.canvas.delete(self.player)
        self.draw_player()
        if self.player_position == self.board_size * self.board_size:
            self.message_label.config(text="Congratulations! You reached the end of the board.")
        else:
            self.message_label.config(text="")
        
    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        self.move_player(dice_roll)

def main():
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
