#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'evenForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t_nodes
#  2. INTEGER t_edges
#  3. LIST[LIST[INTEGER]] t_from
#  4. LIST[LIST[INTEGER]] t_to
#

def evenForest(t_nodes, t_edges, t_from, t_to):
    # Build adjacency list
    adj = [[] for _ in range(t_nodes + 1)]
    for i in range(t_edges):
        u = t_from[i]
        v = t_to[i]
        adj[u].append(v)
        adj[v].append(u)
    
    # DFS to compute subtree sizes and count even subtrees
    count = 0
    visited = [False] * (t_nodes + 1)
    
    def dfs(node, parent):
        nonlocal count
        visited[node] = True
        size = 1
        for child in adj[node]:
            if not visited[child] and child != parent:
                child_size = dfs(child, node)
                if child_size % 2 == 0:
                    count += 1
                size += child_size
        return size
    
    dfs(1, -1)  # Start from node 1
    return count

if __name__ == '__main__':
    # For local testing, read from input.txt
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    t_nodes, t_edges = map(int, lines[0].rstrip().split())
    
    t_from = []
    t_to = []
    
    for i in range(1, t_edges + 1):
        t_from_temp, t_to_temp = map(int, lines[i].rstrip().split())
        t_from.append(t_from_temp)
        t_to.append(t_to_temp)
    
    res = evenForest(t_nodes, t_edges, t_from, t_to)
    
    print(res)
