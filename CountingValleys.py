#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    past = 0
    cur = 0
    for val in s:
        if cur == -1 and past == 0:
            count += 1
        past = cur
        if val == 'D':
            cur -= 1
        else:
            cur += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
