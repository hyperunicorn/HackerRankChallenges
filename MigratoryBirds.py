#!/bin/python

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    countAr = [0,0,0,0,0]
    for val in arr:
        countAr[val - 1] += 1
    maxi = max(countAr)
    i = 0
    while i < 5:
        if countAr[i] == maxi:
            return i + 1
        i += 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
