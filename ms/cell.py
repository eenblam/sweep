from random import random

class Cell(object):
    def __init__(self, board, i, j, p):
        self.board = board
        self.i = i
        self.j = j
        self.mine = random() < p
        self.revealed = False

    def __str__(self):
        self.char = "@" if self.mine else str(self.count_neighbors())
        if self.revealed:
            return self.char
        return "X"

    def count_neighbors(self):
        return self.board.count_neighbors(self.i, self.j)

