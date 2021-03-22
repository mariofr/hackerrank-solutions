# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter
# Complete the isValid function below.
def isValid(s):
    if len(s) == 1: return "YES"
    c = Counter(s)
    v = list(c.values())
    v.sort()
    if v[0] == v[-1]:
        return "YES"
    elif v[-1] == v[-2] + 1 and v[0] == v[-2]:
        return "YES"
    elif v[0] == 1 and v[1] == v[-1]:
        return "YES"
    else:
        return "NO"
        