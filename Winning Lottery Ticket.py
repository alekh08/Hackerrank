#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'winningLotteryTicket' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY tickets as parameter.
#
from collections import Counter

def winningLotteryTicket(tickets):
    
    # Convert each ticket to a bitmask
    def get_bitmask(ticket):
        bitmask = 0
        for digit in ticket:
            bitmask |= 1 << (ord(digit) - ord('0'))
        return bitmask
    
    # Count occurrences of each bitmask
    bitmask_count = Counter(get_bitmask(ticket) for ticket in tickets)
    
    # All possible digits present bitmask (1111111111 in binary = 1023)
    full_mask = (1 << 10) - 1
    
    # Count valid pairs
    total_pairs = 0
    bitmasks = list(bitmask_count.keys())
    
    # Iterate over all pairs of bitmasks
    for i in range(len(bitmasks)):
        for j in range(i, len(bitmasks)):
            if (bitmasks[i] | bitmasks[j]) == full_mask:
                if i == j:
                    total_pairs += bitmask_count[bitmasks[i]] * (bitmask_count[bitmasks[i]] - 1) // 2
                else:
                    total_pairs += bitmask_count[bitmasks[i]] * bitmask_count[bitmasks[j]]
    
    return total_pairs

# Example Usage
tickets = ["129300455", "5559948277", "012334556", "56789", "1234567890"]
print(winningLotteryTicket(tickets))  # Output: 5


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()
