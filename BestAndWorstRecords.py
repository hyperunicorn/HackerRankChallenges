#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxi = scores[0]
    mini = scores[0]
    maxi_count = 0
    mini_count = 0
    for val in scores[1:]:
        if val > maxi:
            maxi = val
            maxi_count += 1
        if val < mini:
            mini = val
            mini_count += 1
    return [maxi_count, mini_count]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
