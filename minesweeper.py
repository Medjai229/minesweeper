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

        # Setup size
        self.size = 10
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
                                     image=self.images["tile"])
                }
                tile["button"].grid(row=x, column=y)
                self.grid[x][y] = tile


if __name__ == "__main__":
    window = Tk()
    window.title("Minesweeper")
    game = Minesweeper(window)
    window.mainloop()
