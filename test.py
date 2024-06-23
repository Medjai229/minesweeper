""" Minesweeper game code """
from tkinter import *
from random import randint


class Minesweeper:
    """ Our game class """

    def __init__(self, tk):
        """ Initialize the game """

        # Create the frame
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()

        # Create time, mines,flags here later

        # Setup iamges
        self.images = {
            "tile": PhotoImage(file="images/unclicked_tile.png"),
            "mine": PhotoImage(file="images/unclicked_mine_tile.png"),
            "flag": PhotoImage(file="images/flag_tile.png"),
            "clicked_mine": PhotoImage(file="images/clicked_mine_tile.png"),
            "wrong_flag": PhotoImage(file="images/wrong_flag_tile.png"),
            "numbers": []
        }
        for i in range(0, 9):
            self.images["numbers"].append(
                PhotoImage(file="images/num{}_tile.png".format(str(i))))

        # Setup size & mines
        self.size = 10
        self.selected_mines = 10
        self.start()

    def start(self):
        """ Start the game """

        # Create the grid
        self.grid = {}
        for x in range(0, self.size):
            for y in range(0, self.size):
                if y == 0:
                    self.grid[x] = {}
                tile = {
                    "button": Button(self.frame,
                                     image=self.images["tile"]),
                    "is_mine": False,
                    "surrounding_mines": 0,
                    "is_flagged": False,
                    "is_clicked": False,
                    "x": x,
                    "y": y
                }
                tile["button"].grid(row=x, column=y)
                self.grid[x][y] = tile

        
        self.mines = 0
        while True:
            self.create_mine()
            if self.mines == self.selected_mines:
                break
        self.check_mines()
        

    def create_mine(self):
        """ Create mines """
        for x in self.grid:
            for y in self.grid[x]:
                if self.grid[x][y]["is_mine"] == True:
                    continue
                if randint(0, (self.size ** 2 + 1) //
                           (self.selected_mines) + 1) == 0:
                    self.grid[x][y]["is_mine"] = True
                    self.grid[x][y]["button"].config(
                        image=self.images["mine"])
                    self.mines += 1
                if self.mines == self.selected_mines:
                    return

    def check_mines(self):
        """ Check surrounding mines """
        for x in self.grid:
            for y in self.grid[x]:
                if self.grid[x][y]["is_mine"] == True:
                    continue
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if x + i < 0 or y + j < 0:
                            continue
                        if x + i > self.size - 1 or y + j > self.size - 1:
                            continue
                        if self.grid[x + i][y + j]["is_mine"] == True:
                            self.grid[x][y]["surrounding_mines"] += 1
                self.grid[x][y]["button"].config(
                    image=self.images["numbers"]
                    [self.grid[x][y]["surrounding_mines"]])


if __name__ == "__main__":
    window = Tk()
    window.title("Minesweeper")
    game = Minesweeper(window)
    window.mainloop()
