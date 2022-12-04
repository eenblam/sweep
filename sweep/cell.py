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
        # Guard against loops
        if self.revealed:
            return

        # Reveal self
        self.revealed = True

        # Reveal any zero-valued neighbors without mines:
        for neighbor in self.valid_neighbors():
            # Be sure neighbor isn't already revealed so we don't get caught in a loop!
            if not neighbor.revealed and not neighbor.mine and not neighbor.count_neighbors():
                neighbor.reveal()

        # If this has a neighboring mine, don't reveal additional neighbors
        if self.count_neighbors():
            return

        # Zero-valued, so show remaining non-mine neighbors
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
