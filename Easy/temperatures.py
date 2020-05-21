# Températures

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
temp = []
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    temp.append(t)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
temp_abs = list(map(lambda x: abs(x), temp))

if len(temp_abs) != 0:
    result = temp[temp_abs.index(min(temp_abs))]
    if result < 0 and -result in temp:
        result = -result
else:
    result = 0

print(result)
