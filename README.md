# Sweep.py
Sweep is a CLI version of a [game you might have played](https://en.wikipedia.org/wiki/Minesweeper_(video_game)).

To play, provide the number of rows and columns, respectively,
as command line arguments.
For example, to play a field of dimension 4x6:

```bash
$ sweep.py 4 6
```

By default, each cell has a 20% chance of being a mine.
You can adjust this by passing a third argument between 0 and 1.
We can extend the above example so that each cell has a 55% chance of being a mine:

```bash
$ sweep.py 4 6 0.55
```

Instructions on how to play are given within the game.

## Example Play

```bash
b@tincan:~/b/gh/eenblam/sweep$ ./sweep.py -h        
Wrong number of arguments 
                         
Usage:   
sweep.py <rows> <columns> [<probability>]
                         
Play:    
Check a cell to see how many mines are adjacent to it.
...but try not to check cells containing mines!
Flag any cells you're sure contain mines.
Flag all the mines (with no mistakes) without triggering one to win.
                         
Note: (0,0) is the top-left cell.
                         
Symbols:
0-8 : the number of adjacent mines
F : a cell you've flagged. Flag again to remove.
@ : a mine
% : a cell you selected that contained a mine
b@tincan:~/b/gh/eenblam/sweep$ ./sweep.py 5 5
Please provide a coordinate of the form "<command> <row> <col>"
where <command> is either "check" or "flag"
and <row> < 5 and <col> < 5.
Or, to quit, simply enter "quit".
X X X X X
X X X X X
X X X X X
X X X X X
X X X X X
check 0 0
0 0 0 1 X
2 3 2 2 X
X X X X X
X X X X X
X X X X X
flag 2 0
0 0 0 1 X
2 3 2 2 X
F X X X X
X X X X X
X X X X X
flag 2 1
0 0 0 1 X
2 3 2 2 X
F F X X X
X X X X X
X X X X X
flag 2 2
0 0 0 1 X
2 3 2 2 X
F F F X X
X X X X X
X X X X X
check 2 3
0 0 0 1 X
2 3 2 2 X
F F F 3 X
X X X X X
X X X X X
check 0 4
Mine!
0 0 0 1 %
2 3 2 2 1
F F F 3 1
3 5 @ @ 1
@ 2 2 2 1
Enter "new" for a new game or "quit" to quit.
```
