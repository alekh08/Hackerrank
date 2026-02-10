#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    m, n = len(a), len(b)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    for i in range(1, m + 1):
        for j in range(n + 1):
            if a[i-1].islower():
                # Can skip
                dp[i][j] = dp[i-1][j]
                # Or capitalize and match if possible
                if j > 0 and a[i-1].upper() == b[j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-1]
            else:
                # Uppercase must match, cannot skip
                if j > 0 and a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1]
    
    return "YES" if dp[m][n] else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input().strip()

        b = input().strip()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
