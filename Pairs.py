# https://www.hackerrank.com/challenges/pairs/problem

from collections import Counter

# Complete the pairs function below.
def pairs(k, arr):
    total = 0
    c = Counter(arr)
    for x in arr:
        y = x + k
        if y in c:
            total += 1
    return total
    