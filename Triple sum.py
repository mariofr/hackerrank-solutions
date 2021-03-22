# https://www.hackerrank.com/challenges/triple-sum/problem

import bisect
# Complete the triplets function below.
def triplets(a, b, c):
	# Remove duplicates
    a = list(set(a))
    a.sort()
    c = list(set(c))
    c.sort()
    b = list(set(b))
    result = 0
    for x in b:
        i = bisect.bisect_right(a, x)
        j = bisect.bisect_right(c, x)
        result += i * j
    return result