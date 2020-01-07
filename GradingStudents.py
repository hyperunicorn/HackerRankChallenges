#!/bin/python

import math
import os
import random
import re
import sys

def customRound(grade):
    if grade < 38:
        return grade
    diff = grade % 5
    if diff >= 3:
        return grade + (5 - diff)
    else:
        return grade

def gradingStudents(grades):
    roundedGrades = []
    for val in grades:
        roundedGrades.append(customRound(val))
    return roundedGrades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(raw_input().strip())

    grades = []

    for _ in xrange(grades_count):
        grades_item = int(raw_input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
