class Game(object):
    def __init__(self):
        pass

    def start(self):
        """Start a new game."""
        pass

    def select(self):
        """Select a coordinate pair to test."""
        pass

    def mine(self):
        """End the game with a loss."""
        pass

    def clear(self):
        """End the game with a win."""
        pass

    def exit(self):
        """Clean up any resources and exit."""
        pass

    def restart(self):
        """Restart the current game.
        
        I.e. reset visibility but not mine distribution.
        """
        pass
