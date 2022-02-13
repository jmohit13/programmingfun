#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

# Terminated due to timeout :(

recursion_counter = 1

def superDigit(n, k):
    # Write your code here
    global recursion_counter

    if recursion_counter == 1:
        input_number = str(n)*k
        recursion_counter += 1
        return superDigit(input_number,k)
    else:
        psum = 0; summed_num_len = 0
        sum_of_digits = sum([psum+int(i) for i in n])

        if len(str(sum_of_digits)) != 1:
            return superDigit(str(sum_of_digits), k)
        elif len(str(sum_of_digits)) == 1:

            return sum_of_digits

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print("2 ",result)
    fptr.write(str(result) + '\n')

    fptr.close()
