# https://www.hackerrank.com/challenges/greedy-florist/problem

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if k >= len(c):
        return sum(c)
    c.sort(reverse=True)
    total = 0
    nPurch = len(c) // k
    remain = len(c) % k
    for i in range(nPurch):
        for j in range(k):
            total += c[i*k + j] * (i+1)
    if remain != 0:
        total += sum(c[-remain:]) * (nPurch+1)
    return total
