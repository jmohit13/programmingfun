#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    beautifulNumbers = 0
    if i <= j:
        for i in range(i,j+1):
            reversed_num = [str(i)[n] for n in range(len(str(i))-1,-1,-1)]
            reversed_num = int("".join(reversed_num))
            if (i - reversed_num) % k == 0:
                beautifulNumbers += 1
        return beautifulNumbers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
