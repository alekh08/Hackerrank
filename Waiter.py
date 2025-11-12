#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#


def waiter(number, q):

    def generate_primes(n):
        primes = []
        num = 2
        while len(primes) < n:
            for p in primes:
                if num % p == 0:
                    break
            else:
                primes.append(num)
            num += 1
        return primes
    primes = generate_primes(q)
    answers = []
    A = number[:]  # Top of stack is the end of the list

    for i in range(q):
        B = []
        next_A = []
        while A:
            plate = A.pop()
            if plate % primes[i] == 0:
                B.append(plate)
            else:
                next_A.append(plate)
        while B:
            answers.append(B.pop())
        A = next_A

    while A:
        answers.append(A.pop())

    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
