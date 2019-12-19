#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    out = 0
    for val in ar:
        out += val
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = simpleArraySum(ar)