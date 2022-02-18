#!/bin/python3

import math
import os
import random
import re
import sys
import inspect

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    not_imp_contest = [i for i in contests if i[1] == 0]
    not_imp_luck = sum([i[0] for i in not_imp_contest])

    imp_contest = [i for i in contests if i[1] == 1]
    imp_contest = sorted(imp_contest, reverse=True)
    # print(inspect.signature(sorted))
    imp_contest_subset = imp_contest[:k]

    imp_contest_luck = sum([i[0] for i in imp_contest_subset])
    contest_to_win = sum([i[0] for i in imp_contest[k:]])

    return (imp_contest_luck + not_imp_luck - contest_to_win)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
