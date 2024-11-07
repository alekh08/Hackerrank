#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter

def isValid(s):
    # Step 1: Count the frequency of each character
    char_count = Counter(s)
    
    # Step 2: Count how many times each frequency appears
    freq_count = Counter(char_count.values())
    
    # If there is only one frequency, it's already valid
    if len(freq_count) == 1:
        return "YES"
    
    # Step 3: If there are exactly two different frequencies
    if len(freq_count) == 2:
        # Get the two frequencies and their respective counts
        (freq1, count1), (freq2, count2) = freq_count.items()
        
        # Check if one of the frequencies is 1, and it occurs once
        if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
            return "YES"
        
        # Check if the difference between the two frequencies is 1,
        # and the higher frequency occurs exactly once
        if abs(freq1 - freq2) == 1:
            if (freq1 > freq2 and count1 == 1) or (freq2 > freq1 and count2 == 1):
                return "YES"
    
    # If none of the conditions are met, the string is not valid
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
