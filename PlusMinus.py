#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    posCount = 0
    negCount = 0
    zeroCount = 0
    for val in arr:
        if val > 0:
            posCount += 1
        if val == 0:
            zeroCount += 1
        if val < 0:
            negCount += 1
    
    pFraction = 1.0 * posCount / length
    zFraction = 1.0 * zeroCount / length
    nFraction = 1.0 * negCount / length
    print("% .6f" % (pFraction))
    print("% .6f" % (nFraction))
    print("% .6f" % (zFraction))
 

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
