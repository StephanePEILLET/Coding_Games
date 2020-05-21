# there-is-no-spoon-episode-1

import sys
import math

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lines=[]

for i in range(height):
    line = input()  # width characters, each either 0 or .
    lines.append(line)

def go_right(i, j, c):
    if j+c < width:
        if lines[i][j+c] == '.':
            return go_right(i,j, c+1)
        else:
            return [j+c, i]
    else:
        return [-1, -1]

def go_down(i, j, c):
    if i+c < height:
        if lines[i+c][j] == '.':
           return go_down(i, j, c+1)
        else:
            return [j, i+c]
    else:
        return [-1, -1]

for i in range(height):
    for j in range(width):
        if lines[i][j] == '0':
            response = [j, i]
            response.extend(go_right(i, j, 1))
            response.extend(go_down(i, j, 1))
            print(' '.join(map(str,response)))
