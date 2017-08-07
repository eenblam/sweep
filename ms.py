#!/usr/bin/env python
from ms import game

def usage(err_msg):
    print(err_msg)
    print("Usage:")
    print("ms <rows> <columns> [<probability>]")
    sys.exit(1)

def match_dimensions(args):
    pass

def match_dimensions_and_probability(s):
    pass

if __name__ == '__main__':
    import sys
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

    game = game.Game(rows, cols, probability)
    game.start()
