# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

from collections import Counter
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    ca = Counter(a)
    cb = Counter(b)
    ca.subtract(cb)
    dels = sum(abs(i) for i in ca.values())
    return dels
