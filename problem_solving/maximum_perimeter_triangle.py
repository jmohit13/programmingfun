#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

# failed 8 test cases

def maximumPerimeterTriangle(sticks):
    # Write your code here
    # Given a,b,c are sides of triangle, then a+b>c, a+c>b, b+c>a

    triangle_triplets = list(set(combinations(sticks,3)))
    triplets = []

    for i in triangle_triplets:
        if i[0] + i[1] > i[2]:
            if i[0] + i[2] > i[1]:
                if i[1] + i[2] > i[0]:
                    triplets.append(i)
    triplets = [list(ele) for ele in triplets]
    print(triplets, len(triplets))

    trip_tup = []

    if len(triplets) > 1:
        for i in triplets:
            trip_tup.append((i, sum(i)))
        return "".join(str(i) for i in max(trip_tup)[0])
    elif len(triplets) == 0:
        return [-1]
    else:
        sorted_triplet = sorted(triplets, reverse=True)
        # sorted_triplet = [list(ele) for ele in sorted_triplet]
        print(len(triplets), triplets, list(sorted_triplet))
        return "".join(str(i) for i in max(sorted_triplet))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
