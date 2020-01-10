#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if p == 1 or p == n:
        return 0
    else:
        if p <= n / 2:
            if p % 2 == 0:
                return int(p / 2)
            else:
                return int((p-1)/2)
        else:
            if p % 2 == 0:
                return int((n - p)/2)
            else:
                return int((n - p + 1)/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
