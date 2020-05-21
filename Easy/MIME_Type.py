# MIME Type

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

ext_elements = []
mt_elements = []
q_elements = []
result = []

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext_elements.append(ext.lower())
    mt_elements.append(mt)

for i in range(q):
    fname = input()  # One file name per line.
    q_elements.append(fname)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

def is_ext(ext):
    ext = ext.lower()
    if ext in ext_elements:
        result.append(mt_elements[ext_elements.index(ext)])
    else:
        result.append("UNKNOWN")

for f in q_elements:
    if '.' in f and len(f.split('.')) >= 2:
        file = f.split('.')[0]
        ext = f.split('.')[-1]
        is_ext(ext)
    else:
        result.append("UNKNOWN")

'''
print(ext_elements)
print(mt_elements)

beautiful_disp = {}
for x, y in zip(q_elements, result):
    beautiful_disp[x] = y

print(beautiful_disp)
'''

for el in result:
    print(el)
