#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    
    w = list(w)
    i = len(w) - 2

    # Step 1: Find the longest non-increasing suffix
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1

    if i == -1:
        return "no answer"

    # Step 2: Find the rightmost successor to the pivot
    j = len(w) - 1
    while w[j] <= w[i]:
        j -= 1

    # Step 3: Swap the pivot with successor
    w[i], w[j] = w[j], w[i]

    # Step 4: Reverse the suffix
    w[i + 1:] = reversed(w[i + 1:])
    return ''.join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
