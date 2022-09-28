#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    strLen = len(grid[0])
    grid_ascii = [ord(i) for alphaStr in grid for i in alphaStr]

    s = 0; e = strLen; grid_num = []
    for i in range(0,int(len(grid_ascii)/strLen)):
        grid_num.append(grid_ascii[s:e])
        # print(grid_num)
        s = e; e += strLen
    # print(grid_ascii)

    # sort the rows
    grid_num_rowsort = [sorted(i,reverse=False) for i in grid_num]
    # then check if the columns values are in proper order
    grid_num_colwise = []

    itr = 0
    while itr < strLen:
        for i in grid_num_rowsort:
            grid_num_colwise.append(i[itr])
        itr += 1
    print(grid_num_rowsort)
    print(grid_num_colwise)

    s2 = 0; e2 = strLen; grid_num_col = []
    for i in range(0,int(len(grid_num_colwise)/strLen)):
        grid_num_col.append(grid_num_colwise[s2:e2])
        s2 = e2; e2 += strLen
    print(grid_num_col)

    itr2 = 0; colFlag = False; i = 0
    while itr2 < len(grid_num_col):

        for eachList in grid_num_col:
            for j in eachList:
                print(j, eachList)
                if eachList[i] < eachList[i+1]:
                    colFlag = True
                else:
                    colFlag = False

            print(colFlag)
        break

    if colFlag == True:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
