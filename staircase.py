#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    sp = n - 1
    step = 1
    while sp >= 0:
        print (" " * sp) + ("#" * step)
        sp -= 1
        step += 1

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
