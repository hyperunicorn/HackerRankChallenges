#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mini = 5 * 10**9
    maxi = 0
    for i in range(len(arr)):
        tmp = excludedSum(arr, i)
        if tmp < mini:
            mini = tmp
        if tmp > maxi:
            maxi = tmp
    print(str(mini) + " " + str(maxi))

def excludedSum(arr, index):
    i = 0
    sm = 0
    while i < len(arr):
        if i != index:
            sm += arr[i]
    return sm

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
