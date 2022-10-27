#!/usr/bin/env python3
import sys

from .game import Game

def usage(err_msg):
    print(err_msg)
    print()
    print("Usage:")
    print("sweep.py <rows> <columns> [<probability>]")
    print()
    print("Play:")
    print("Check a cell to see how many mines are adjacent to it.")
    print("...but try not to check cells containing mines!")
    print("Flag any cells you're sure contain mines.")
    print("Flag all the mines (with no mistakes) without triggering one to win.")
    print()
    print("Note: (0,0) is the top-left cell.")
    print()
    print("Symbols:")
    print("0-8 : the number of adjacent mines")
    print("F : a cell you've flagged. Flag again to remove.")
    print("@ : a mine")
    print("% : a cell you selected that contained a mine")
    sys.exit(1)

def run():
    if len(sys.argv) not in (3, 4):
        usage("Wrong number of arguments")

    try:
        rows = int(sys.argv[1])
    except ValueError:
        usage("Could not parse number of rows")
    try:
        cols = int(sys.argv[2])
    except ValueError:
        usage("Could not parse number of columns")

    if len(sys.argv) == 4:
        try:
            probability = float(sys.argv[3])
        except ValueError:
            usage("Could not parse probability as float")

        if probability > 1 or probability <= 0:
            usage("Probability must be between 0 and 1, exclusively")
    else:
        probability = 0.2

    game = Game(rows, cols, probability)
    game.start()

