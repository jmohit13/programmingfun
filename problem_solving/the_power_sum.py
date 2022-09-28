#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import islice

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

# total_sum = 0
powerSum_count = 0
num_list = []

def powerSum(X, N):
    # Write your code here

    # global total_sum
    global powerSum_count
    global num_list

    root_x = X ** (1/N)
    num_list = [i for i in range(1,int(root_x)+1)]

    # Execute only once
    if (X ** (1/N)) % N == 0:
        powerSum_count += 1

    if total_sum != X:
        for i in range(0,len(num_list)):
            for j in range(i+1,len(num_list)):
                total_sum = 0
                total_sum += pow(num_list[i],N) + pow(num_list[j],N)
                print(num_list[i], num_list[j], total_sum)
                if total_sum != X:
                    return powerSum(X, N)

    print(root_x, num_list, powerSum_count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
