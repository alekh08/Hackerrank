#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#


sys.setrecursionlimit(10**6)

def cutTheTree(data, edges):
    from collections import defaultdict

    n = len(data)
    tree = defaultdict(list)
    for u, v in edges:
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)

    total = sum(data)
    visited = [False] * n
    subtree_sum = [0] * n
    min_diff = float('inf')

    def dfs(node):
        nonlocal min_diff
        visited[node] = True
        curr_sum = data[node]
        for neighbor in tree[node]:
            if not visited[neighbor]:
                curr_sum += dfs(neighbor)
        subtree_sum[node] = curr_sum
        diff = abs(total - 2 * curr_sum)
        min_diff = min(min_diff, diff)
        return curr_sum

    dfs(0)
    return min_diff
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
