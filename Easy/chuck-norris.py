#chuck-norris

import sys
import math
from itertools import groupby
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
message = input()
list_bits = (format(ord(x), 'b') for x in message)
message_bit = ''.join(['0'*(7-len(bits)) + bits if len(bits) < 7 else bits for bits in list_bits])
filter_spaces = filter(lambda x: x != " ", message_bit)
message_no_space = ''.join(filter_spaces)
grouped = [''.join(letter) for _, letter in groupby(message_no_space)]
dict_values = {'1' : '0', '0':'00'}
out = []
for g in grouped:
    len_g = len(g)
    time_zeros = '0'*len_g
    out.append(dict_values[g[0]])
    out.append(time_zeros)
print(' '.join(out))c
