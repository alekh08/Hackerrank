#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):

    h.append(0)  
    stack = []
    max_area = 0

    for i in range(len(h)):
        start=i
        while stack and stack[-1][0] > h[i]:
            height, start = stack.pop()
            max_area = max(max_area, height * (i - start))
        stack.append((h[i], start))

    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
