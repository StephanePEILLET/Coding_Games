# shadows-of-the-knight-episode-1

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
x_bat, y_bat = x0, y0

class Switcher(object):
    def __init__(self):
        self.x_bat = x0
        self.y_bat = y0

        # Define visited area bounds
        self.lefterbound = 0
        self.righterbound = w
        self.upperbound = 0
        self.lowerbound = h

        # Module offset for the tower test for the submission
        self.prec = ''
        self.ante = ''
        self.offset = 1
        self.action = 0

    def actions(self, argument):
        method_name = 'move_' + argument
        method = getattr(self, method_name, lambda: "Invalid move")

        if argument == self.prec and argument == self.ante and self.action <5:
            self.offset = 0
        else:
            self.offset = 1

        self.ante = self.prec
        self.prec = argument
        self.action += 1

        return method()

    def move_L(self):
        self.righterbound = self.x_bat - 1
        if math.floor((self.x_bat - self.lefterbound)/2) > 1:
            self.x_bat -= math.floor((self.x_bat - self.lefterbound)/2) + self.offset
        else:
           self.x_bat -= 1

    def move_R(self):
        self.lefterbound = self.x_bat + 1
        if math.floor((self.righterbound - self.x_bat)/2) > 1:
            self.x_bat += math.floor((self.righterbound - self.x_bat)/2) + self.offset
        else:
            self.x_bat += 1

    def move_U(self):
        self.lowerbound = self.y_bat - 1
        if math.floor((self.y_bat - self.upperbound)/2) > 1:
            self.y_bat -= math.floor((self.y_bat - self.upperbound)/2) + self.offset
        else:
            self.y_bat -= 1

    def move_D(self):
        self.upperbound = self.y_bat + 1
        if math.floor((self.lowerbound - self.y_bat)/2) > 1:
            self.y_bat += math.floor((self.lowerbound - self.y_bat)/2) + self.offset
        else:
            self.y_bat += 1

    def move_UR(self):
        self.move_U()
        self.move_R()

    def move_DL(self):
        self.move_D()
        self.move_L()

    def move_UL(self):
        self.move_U()
        self.move_L()

    def move_DR(self):
        self.move_D()
        self.move_R()

    def get_coord(self):
        print("{0} {1}".format(self.x_bat,self.y_bat))

switcher = Switcher()

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    # Write an action using print
    # the location of the next window Batman should jump to.

    switcher.actions(bomb_dir)
    switcher.get_coord()

'''
##### Code optim #####

import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]
x, y = 0, 0
x1, y1 = w, h

while True:
    bomb_dir = input()
    if "R" in bomb_dir:
        x = x0
    elif "L" in bomb_dir:
        x1 = x0
    if "U" in bomb_dir:
        y1 = y0
    elif "D" in bomb_dir:
        y = y0

    x0 = int((x1+x)/2)
    y0 = int((y1+y)/2)
    print(x0, y0)
'''
