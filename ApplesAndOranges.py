#!/bin/python

import math
import os
import random
import re
import sys

def inInterval(val, start, end):
    return val >= start and val <= end

    

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    numApples = 0
    numOranges = 0
    for val in apples:
        if inInterval(a + val, s, t):
            numApples += 1
    for val in oranges:
        if inInterval(b + val, s, t):
            numOranges += 1
    print(numApples)
    print(numOranges)
if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)
