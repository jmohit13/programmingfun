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

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    i = 0
    if x2 > x1:
        if v2 > v1:
            return "NO"
        # while True:


        # else:
        #     kangaro1_dist = x1 + v1
        #     kangaro2_dist = x2 + v2

        #     if kangaro1_dist == kangaro2_dist:
        #         return "YES"

        #     kangaro1_dist += v1
        #     kangaro2_dist += v2
        #     print("i",i)
        #     i += 1


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
