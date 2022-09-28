#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    total = 0; result = 0

    bill_cost = bill[:k] + bill[k+1:]

    for i in bill_cost:
        total += i

    anna_share = total/2

    if b > anna_share:
        result = int(b - anna_share)
    elif b == anna_share:
        result = "Bon Appetit"

    print(result)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
