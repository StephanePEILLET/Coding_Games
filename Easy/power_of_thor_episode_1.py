# power-of-thor-episode-1

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

class Thor(object):
    def __init__(self):
        self.thor_x = initial_tx
        self.thor_y = initial_ty

    def move(self):
        if self.thor_x > light_x and (self.thor_x >= 0 and self.thor_x <= 40):
            if self.thor_y >= 0 and self.thor_y <= 17 and (self.thor_y  != light_y):
                if self.thor_y  < light_y:
                    print('SW')
                    self.thor_x -= 1
                    self.thor_y += 1
                else: #self.thor_y  > light_y
                    print('NW')
                    self.thor_x -= 1
                    self.thor_y -= 1
            else: # thor_y == light_y
                print('W')
                self.thor_x -=  1
        elif self.thor_x < light_x and (self.thor_x >= 0 and self.thor_x <= 40):
            if self.thor_y >= 0 and self.thor_y <= 17 and (self.thor_y  != light_y):
                if self.thor_y  < light_y:
                    print('SE')
                    self.thor_x += 1
                    self.thor_y += 1
                else: #self.thor_y  > light_y
                    print('NE')
                    self.thor_x +=  1
                    self.thor_y -= 1
            else: # thor_y == light_y
                print('E')
                self.thor_x +=  1
        else: # thor_x == light_x
            if self.thor_y  < light_y:
                print('S')
                self.thor_y += 1
            if self.thor_y  > light_y:
                print('N')
                self.thor_y -= 1

thor = Thor()

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    #print('remaining_turns:', remaining_turns)
    thor.move()

    # A single line providing the move to be made: N NE E SE S SW W or NW

    # print("Debug messages...", file=sys.stderr)
