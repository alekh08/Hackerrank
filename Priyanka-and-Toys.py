#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#
def toys(w):
    w.sort()  # Step 1: sort weights
    n = len(w)
    
    containers = 0
    i = 0
    
    while i < n:
        containers += 1
        
        # Current box range
        limit = w[i] + 4
        
        # Skip all toys within range
        while i < n and w[i] <= limit:
            i += 1
    
    return containers


#  Example usage
# n = 8
# w = [1, 2, 3, 21, 7, 12, 14, 21]

# print(toys(w))  # Output: 4

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
