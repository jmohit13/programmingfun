#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here

    final_grade = []

    for grade in grades:
        if grade < 38:
            final_grade.append(grade)
        else:
            if (5 - (grade % 5)) in [1]:
                final_grade.append(grade+1)
            elif (5 - (grade % 5)) in [2]:
                final_grade.append(grade+2)
            else:
                final_grade.append(grade)

    return final_grade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
