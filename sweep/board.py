from .cell import Cell
from .result import Result

class Board(object):
    def __init__(self, m, n, p=0.2):
        self.m = m
        self.n = n
        self.board = [[]] * m
        self.num_mines = 0
        for i in range(m):
            self.board[i] = [None] * n
            for j in range(n):
                new_cell = Cell(self, i, j, p)
                self.num_mines += new_cell.mine
                self.board[i][j] = new_cell

    def count_neighbors(self, i, j):
        # Check within bounds
        if not self.valid_position(i, j):
            raise ValueError("Position ({},{}) not valid on {}x{} board"
                    .format(i, j, self.m, self.n))

        count = 0
        for neighbor in self.valid_neighbors(i, j):
            count += neighbor.mine

        return count

    def valid_neighbors(self, i, j):
        offsets = (-1, 0, 1)
        for x in offsets:
            for y in offsets:
                if (x,y) == (0,0):
                    continue
                a = i + x
                b = j + y
                if self.valid_position(a, b):
                    yield self.board[a][b]

    def valid_position(self, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return False
        return True

    def __str__(self):
        return  "\n".join(
                " ".join(str(cell) for cell in row)
                for row in self.board)

    def _reveal_board(self):
        """Debug mode for board."""
        for row in self.board:
            for cell in row:
                cell.revealed = True

        return str(self)

    def check(self, i, j):
        """Reveal position (i,j).

        Also reveal any neighboring cells with counts of 0.
        """
        if not self.valid_position(i, j):
            # Return invalid input message
            return Result(message="Invalid position ({},{}) on {}x{} board."
                    .format(i, j, self.m, self.n),
                    code=0)

        target = self.board[i][j]
        if target.revealed:
            return Result(message="Cell ({},{}) already revealed."
                    .format(i, j),
                    code=0)

        if target.flagged:
            return Result(message="Cell ({},{}) is currently flagged. Unflag to check with \"flag {} {}\"."
                    .format(i, j, i, j),
                    code=0)

        if target.mine:
            target.fatal = True
            return Result(message="Mine!", code=-1)

        # Reveal cell
        # Recursively reveal all empty neighbors
        target.reveal()
        return Result(message="", code=0)


    def flag(self, i, j):
        """Toggle flag at position (i,j)."""
        if not self.valid_position(i, j):
            # Return invalid input message
            return Result(message="Invalid position ({},{}) on {}x{} board."
                    .format(i, j, self.m, self.n),
                    code=0)

        target = self.board[i][j]
        if target.revealed:
            return Result(message="Cell ({},{}) already revealed."
                    .format(i, j),
                    code=0)

        # Toggle flag:
        delta = target.toggle_flag()
        self.num_mines += delta

        # Check for completion (num_mines == 0)
        if self.num_mines == 0:
            # If complete reveal board and return success result
            self._reveal_board()
            return Result("Success!", 1)

        # Otherwise return continue result
        return Result("", 0)
