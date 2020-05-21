# Dwarfs Standing On The Shoulders Of Giants

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
dico = {}
maxlenght = 0
length = ''
count = 1
all_count = []
all_length = []

n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    if x in dico.keys():
        dico[x].append(y)
    else:
        dico[x] = [y]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)
def parse(key, length, count):
    for el0 in dico[key]:
        tmp =  length + '->' + str(el0)
        tmp_count = count + 1
        if el0 in dico.keys():
            parse(el0, tmp, tmp_count)
        else:
            all_length.append(tmp)
            all_count.append(tmp_count)

for key in dico.keys():
    parse(key, str(key), count)
    
'''
print("Debug messages...", file=sys.stderr)
print(dico)
print(all_length)
print(str(max(all_length)))
'''

print(str(max(all_count)))

'''
for key in dico.keys():
    for el0 in dico[key]:
        if el0 in dico.keys():
            lenght += 1
            for el1 in dico[el0]:
                if el1 in dico.keys():
                    lenght += 1
                    for el2 in dico[el1]:
                        if el2 in dico.keys():

'''

# The number of people involved in the longest succession of influences
