#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    likes = []; shares = 0;
    day_n_likes = 5;

    while (n > 0):
        day_n_likes = math.floor(day_n_likes / 2);
        likes.append(day_n_likes)
        day_n_likes = day_n_likes * 3
        n = n - 1

    return sum(likes)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
