#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    
    directions = {
        'N': n - r_q,
        'S': r_q - 1,
        'E': n - c_q,
        'W': c_q - 1,
        'NE': min(n - r_q, n - c_q),
        'NW': min(n - r_q, c_q - 1),
        'SE': min(r_q - 1, n - c_q),
        'SW': min(r_q - 1, c_q - 1)
    }

    for r_o, c_o in obstacles:
        if c_o == c_q:
            if r_o > r_q:
                directions['N'] = min(directions['N'], r_o - r_q - 1)
            else:
                directions['S'] = min(directions['S'], r_q - r_o - 1)
        elif r_o == r_q:
            if c_o > c_q:
                directions['E'] = min(directions['E'], c_o - c_q - 1)
            else:
                directions['W'] = min(directions['W'], c_q - c_o - 1)
        elif abs(r_o - r_q) == abs(c_o - c_q):
            if r_o > r_q and c_o > c_q:
                directions['NE'] = min(directions['NE'], r_o - r_q - 1)
            elif r_o > r_q and c_o < c_q:
                directions['NW'] = min(directions['NW'], r_o - r_q - 1)
            elif r_o < r_q and c_o > c_q:
                directions['SE'] = min(directions['SE'], r_q - r_o - 1)
            elif r_o < r_q and c_o < c_q:
                directions['SW'] = min(directions['SW'], r_q - r_o - 1)

    return sum(directions.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
