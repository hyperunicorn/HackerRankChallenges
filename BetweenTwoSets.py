#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def dividesArray(x, arr):
    for val in arr:
        if x % val != 0:
            return False
    return True

def arrayDivide(x, arr):
    for val in arr:
        if val % x != 0:
            return False
    return True

def getTotalX(a, b):
    intermediate = [x for x in range(1,101) if dividesArray(x, a)]
    final = [x for x in intermediate if arrayDivide(x, b)]
    return len(final)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
