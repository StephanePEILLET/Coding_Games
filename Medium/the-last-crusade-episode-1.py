#the-last-crusade-episode-1

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
lines = []
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    lines.append(line)

ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
lines = [x.split(' ') for x in lines]

def up(x,y):
    return x, y-1

def down(x,y):
    return x, y+1

def left(x,y):
    return x-1, y

def right(x,y):
    return x+1, y

type_0 = {}

type_1 = {'TOP': down,
          'LEFT':down,
          'RIGHT':down}

type_2 = {'LEFT':right,
          'RIGHT':left}

type_3 = {'TOP': down}

type_4 = {'TOP': left,
          'RIGHT': down}

type_5 = {'TOP': right,
          'LEFT': down}

type_6 = {'LEFT':right,
          'RIGHT':left}

type_7 = {'TOP':down,
          'RIGHT':down}

type_8 = {'LEFT':down,
          'RIGHT': down}

type_9 = {'TOP':down,
          'LEFT':down}

type_10 = {'TOP':left}

type_11 = {'TOP': right}

type_12 = {'RIGHT':down}

type_13 = {'LEFT':down}

pieces = { '0': type_0,
        '1': type_1,
        '2': type_2,
        '3': type_3,
        '4': type_4,
        '5': type_5,
        '6': type_6,
        '7': type_7,
        '8': type_8,
        '9': type_9,
        '10': type_10,
        '11': type_11,
        '12': type_12,
        '13': type_13
}

def print_result(x, y):
    print(f"{str(x)} {str(y)}")

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)

    x, y =pieces[lines[yi][xi]][pos](xi, yi)

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(f"{str(x)} {str(y)}")
