#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    subArrays = []
    a = sorted(a)

    for i in range(0,len(a)):
        temp_arr = []
        for j in range(i+1,len(a)):

            if a[j] - a[i] <= 1:
                if a[i] == a[j]:
                    temp_arr.append(a[i])
                else:
                    temp_arr.append(a[i])
                    temp_arr.append(a[j])

        subArrays.append(temp_arr)
    subArrLen = [len(i) for i in subArrays]
    
    return max(subArrLen)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
