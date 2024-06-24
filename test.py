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
                tile["button"].bind("<Button-1>",
                                    lambda Button, x=x, y=y: self.left_click(x, y))
                tile["button"].bind("<Button-3>",
                                    lambda Button, x=x, y=y: self.right_click(x, y))
                tile["button"].grid(row=x, column=y)
                self.tk.bind("r", lambda Res: self.restart())
                self.grid[x][y] = tile

        # Create mines in the grid
        self.mines = 0
        while True:
            # forever loop until the number is met
            self.create_mine()
            if self.mines == self.selected_mines:
                break

        # Check surrounding mines
        self.check_mines()
        

    def restart(self):
        """ Restart the game """
        self.start()


    def create_mine(self):
        """ Create mines """
        for x in self.grid:
            for y in self.grid[x]:
                # add here a condtion that the places where it is initially clicked
                # doesn't have a mine and the same goes for its neighbors
                # --------------------------------
                if self.grid[x][y]["is_mine"] == True:
                    continue
                if randint(0, (self.size ** 2 + 1) //
                           (self.selected_mines) + 1) == 0:
                    self.grid[x][y]["is_mine"] = True
                    #self.grid[x][y]["button"].config(
                        #image=self.images["mine"])
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
                        # if out of boundries top and side
                        if x + i < 0 or y + j < 0:
                            continue
                        # if out of boundries bot and side
                        if x + i > self.size - 1 or y + j > self.size - 1:
                            continue
                        if self.grid[x + i][y + j]["is_mine"] == True:
                            self.grid[x][y]["surrounding_mines"] += 1
                #self.grid[x][y]["button"].config(
                    #image=self.images["numbers"]
                    #[self.grid[x][y]["surrounding_mines"]])


    def left_click(self, x, y):
        """ Left click """
        if self.grid[x][y]["is_flagged"] == True:
            return

        if self.grid[x][y]["is_clicked"] == True:
            return

        elif self.grid[x][y]["is_mine"] == True:
            self.grid[x][y]["button"].config(
                image=self.images["clicked_mine"])

        elif self.grid[x][y]["surrounding_mines"] == 0:
            self.grid[x][y]["button"].config(
                image=self.images["numbers"][0])
            self.grid[x][y]["is_clicked"] = True
            self.clear_surr(x, y)

        else:
            self.grid[x][y]["button"].config(
                image=self.images["numbers"]
                [self.grid[x][y]["surrounding_mines"]])
            self.grid[x][y]["is_clicked"] = True


    def clear_surr(self, x, y):
        """ Clear surrounding tiles """
        for i in range(-1, 2):
            for j in range(-1, 2):
                # if out of boundries top and side
                if x + i < 0 or y + j < 0:
                    continue
                # if out of boundries bot and side
                if x + i > self.size - 1 or y + j > self.size - 1:
                    continue
                #if self.grid[x + i][y + j]["surrounding_mines"] == 0:
                self.left_click(x + i, y + j)


    def right_click(self, x, y):
        """ Right click """
        if self.grid[x][y]["is_clicked"] == True:
            return
        if self.grid[x][y]["is_flagged"] == False:
            self.grid[x][y]["button"].config(image=self.images["flag"])
            self.grid[x][y]["is_flagged"] = True
        else:
            self.grid[x][y]["button"].config(image=self.images["tile"])
            self.grid[x][y]["is_flagged"] = False


if __name__ == "__main__":
    window = Tk()
    window.title("Minesweeper")
    game = Minesweeper(window)
    window.mainloop()
