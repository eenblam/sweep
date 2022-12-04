from .command import GameCommand, MenuCommand
from .board import Board

class Game(object):
    def __init__(self, m, n, p=0.2):
        self.m = m
        self.n = n
        self.p = p
        self.usage()

    def start(self):
        """Start a new game."""
        self.board = Board(self.m, self.n, self.p)
        self.select()

    def select(self):
        """Select a coordinate pair to test."""
        while True:
            print(self.board)
            command = GameCommand(self.m, self.n)
            if not command.valid:
                self.usage()
                continue

            if command.action == 'quit':
                self.exit()

            row = command.row
            col = command.col

            if command.action == 'check':
                result = self.board.check(row, col)
            elif command.action == 'flag':
                result = self.board.flag(row, col)
            else:
                raise RuntimeError("Command listed as valid without valid action")

            if result.message:
                print(result.message)

            if result.code != 0:
                break

        self.end()

    def end(self):
        """End the game, and prompt user to restart or quit."""
        self.board._reveal_board()
        print(self.board)
        print('Enter "new" for a new game or "quit" to quit.')
        while True:
            command = MenuCommand()
            if command.action == 'new':
                self.start()
            elif command.action == 'quit':
                self.exit()
            else:
                self.usage()


    def exit(self):
        """Clean up any resources and exit."""
        import sys
        sys.exit(0)

    def restart(self):
        """Restart the current game.
        
        I.e. reset visibility but not mine distribution.
        """
        pass

    def usage(self):
        print('Please provide a coordinate of the form "<command> <row> <col>"')
        print('where <command> is either "check" or "flag"')
        print('and <row> < {} and <col> < {}.'.format(self.m, self.n))
        print('Or, to quit, simply enter "quit".')

