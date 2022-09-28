#!/bin/python3

import math
import os
import random
import re
import sys
import string


#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#

def crosswordPuzzle(crossword, words):
    # Write your code here
    words = words.split(';')
    rows = []

    for word in words:
        for i in crossword:
            for token in range(0, len(i)-1):
                print(i[token])
                if i[token] == '-':
                    if i[token + 1] == '-':
                        # horizontal word
                        print(word[0], len(word))
                        print(i[token].replace('-', word[0]))
                        updated = i[token].replace('-', word[0])
                        rows.append(updated)
                        if len(word) > 0:
                            print("h replace: ",word[0], word)
                            word = word[1:len(word)]

                    else:
                        # vertical single character
                        print(i[token].replace('-', word[0]))
                        updated = i[token].replace('-', word[0])
                        rows.append(updated)
                        if len(word) > 0:
                            print("v replace: ",word[0], word, len(word))
                            word = word[1:len(word)]
                else:
                    rows.append(i[token])
                print(rows)

    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
