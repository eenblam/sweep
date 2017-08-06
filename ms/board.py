from cell import Cell

class Board(object):
    def __init__(self, m, n, p=0.2):
        self.m = m
        self.n = n
        self.board = [[]] * m
        for i in range(m):
            self.board[i] = [None] * n
            for j in range(n):
                self.board[i][j] = Cell(self, i, j, p)

    def neighbors(self, i, j):
        # Check within bounds
        if i < 0 or j < 0:
            raise ValueError("board does not contain negative indices ({},{})"
                    .format(i, j))
        if i >= self.m or j >= self.n:
            raise ValueError("Position ({},{}) out of range on {}x{} board"
                    .format(i, j, self.m, self.n))

        count = 0
        coordinates = (-1, 0, 1)
        for x in coordinates:
            for y in coordinates:
                if (x,y) != (0,0):
                    count += self.maybe_position(i, j, x, y)

        return count

    def maybe_position(self, i, j, x, y):
        i += x
        j += y
        if i < 0 or j < 0 or i >= self.m or j >= self.n:
            return 0
        return int(self.board[i][j].mine)

    def reveal(self):
        for row in self.board:
            for cell in row:
                cell.revealed = True

        return str(self)

    def __str__(self):
        return  "\n".join(
                " ".join(str(cell) for cell in row)
                for row in self.board)

