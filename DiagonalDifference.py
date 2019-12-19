#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    length = len(arr)
    lrDiag = 0
    rlDiag = 0
    i = 0
    while i < length:
        lrDiag += arr[i][i]
        i += 1
    i = length - 1
    j = 0
    while j < length:
        rlDiag += arr[j][i]
        j += 1
        i -= 1
    return abs(lrDiag - rlDiag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
