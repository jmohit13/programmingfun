#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    ws = 0; bs = 0;
    nws = 0; nbs = 0;

    for idx, i in enumerate(scores):
        if idx == 0:
            ws = i; bs = i
        if i < ws:
            ws = i
            nws += 1
        if i > bs:
            bs = i
            nbs += 1

    return nbs, nws


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
