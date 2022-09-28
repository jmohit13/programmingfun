#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    minPageFromLeft = 0
    minPageFromRight = 0
    pc = 0
    pageLR = []

    def traverseFromLeft(minPageFromLeft, pc, pageLR, p):
        print("1", minPageFromLeft, pc, pageLR, p)
        for i in range(0,p):
            minPageFromLeft += 1
            pc = (pc+1, pc+2)
            if p == pc[0] or p == pc[1]:
                pageLR.append(minPageFromLeft)
            print(minPageFromLeft, pc, pageLR)
            return pageLR

    if p == 1 or p == n or p == n-1:
        # On first or last page
        return pc
    else:
        # any other case
        pageLR = traverseFromLeft(minPageFromLeft, pc, pageLR, p)
        # minPageFromRight += 1

        return min(pageLR)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
