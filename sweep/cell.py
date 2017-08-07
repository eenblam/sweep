from random import random

class Cell(object):
    def __init__(self, board, i, j, p):
        self.board = board
        self.i = i
        self.j = j
        self.mine = random() < p
        self.revealed = False
        self.flagged = False
        self.fatal = False

    def __str__(self):
        fatal = '%'
        mine = '@'
        flag = 'F'
        blank = 'X'

        if self.fatal:
            return fatal
        if self.flagged:
            return flag
        if self.revealed:
            return mine if self.mine else str(self.count_neighbors())
        return blank

    def count_neighbors(self):
        return self.board.count_neighbors(self.i, self.j)

    def valid_neighbors(self):
        return self.board.valid_neighbors(self.i, self.j)

    def reveal(self):
        # Reveal self
        self.revealed = True

        # Reveal neighbors if none are mines
        if self.count_neighbors():
            return

        for neighbor in self.valid_neighbors():
            if not neighbor.revealed:
                neighbor.reveal()

    def toggle_flag(self):
        """Toggle flagged state of cell.

        Return delta in number of mines undetected.
        """
        if not self.mine:
            self.flagged = not self.flagged
            return 0

        # If mine & flagged, unflag and inc num_mines
        if self.flagged:
            self.flagged = False
            return 1
        # If mine & not flagged, flag and dec num_mines
        else:
            self.flagged = True
            return -1
