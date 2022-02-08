#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

# solution 2
# Terminated due to timeout :(

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    # Arithmetic progression a_n = a_0 + (n - 1) * d

    i = 0;
    keep_jumping = True

    if x2 > x1:
        if v2 > v1:
            return "NO"

        n = 1

        while keep_jumping:
            x1_nth = x1 + (n - 1) * v1
            x2_nth = x2 + (n - 1) * v2
            n += 1

            if x1_nth == x2_nth:
                # print(x1_nth)
                keep_jumping = False
                return "YES"

# s1 0 3 4 2
# s2 1 2 4 1
    # 1 2 1 3 5 7
    # 4 1 4 5 6 7

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
