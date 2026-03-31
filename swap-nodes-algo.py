#!/bin/python3

import os
import sys
from collections import deque

# Increase recursion depth to handle deep/skewed trees
sys.setrecursionlimit(2000)

class Node:
    def __init__(self, val, depth):
        self.val = val
        self.depth = depth
        self.left = None
        self.right = None

def swapNodes(indexes, queries):
    # 1. Build the tree using a Queue (Level-order)
    # We also map nodes to their depths for fast access during swaps
    root = Node(1, 1)
    queue = deque([root])
    nodes_by_depth = {1: [root]}
    
    for left_val, right_val in indexes:
        curr = queue.popleft()
        
        # Add left child
        if left_val != -1:
            curr.left = Node(left_val, curr.depth + 1)
            queue.append(curr.left)
            nodes_by_depth.setdefault(curr.depth + 1, []).append(curr.left)
            
        # Add right child
        if right_val != -1:
            curr.right = Node(right_val, curr.depth + 1)
            queue.append(curr.right)
            nodes_by_depth.setdefault(curr.depth + 1, []).append(curr.right)
            
    max_depth = max(nodes_by_depth.keys())
    
    # Helper function for In-order traversal (Left, Root, Right)
    def get_inorder(node, res):
        if node:
            get_inorder(node.left, res)
            res.append(node.val)
            get_inorder(node.right, res)
            
    results = []
    
    # 2. Process each query k
    for k in queries:
        # Identify all levels that are multiples of k (k, 2k, 3k...)
        for depth in range(k, max_depth + 1, k):
            if depth in nodes_by_depth:
                for node in nodes_by_depth[depth]:
                    # Perform the swap
                    node.left, node.right = node.right, node.left
        
        # Capture the result of the in-order traversal after this query's swaps
        current_traversal = []
        get_inorder(root, current_traversal)
        results.append(current_traversal)
        
    return results

if __name__ == '__main__':
    # Standard HackerRank input/output handling
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    n = int(input().strip())
    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    # Format the 2D array result for output
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    if fptr != sys.stdout:
        fptr.close()
