# https://www.hackerrank.com/challenges/crush/problem

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    c = Counter()
    for a,b,k in queries:
        c[a-1] += k
        c[b] -= k
    arrSum = 0
    maxSum = 0
    for i in sorted(c):
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)
    return maxSum
	