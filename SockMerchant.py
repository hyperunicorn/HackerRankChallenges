#!/bin/python3

import math
import os
import random
import re
import sys

def countElements(el, ar):
    count = 0
    for val in ar:
        if val == el:
            count += 1
    return count

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    newAr = list(dict.fromkeys(ar))
    for val in newAr:
        count += (countElements(val, ar)//2)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
