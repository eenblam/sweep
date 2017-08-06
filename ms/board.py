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

    def reveal(self):
        for row in self.board:
            for cell in row:
                cell.revealed = True

        return str(self)
