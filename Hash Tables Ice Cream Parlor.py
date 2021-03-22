# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

from collections import Counter
# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    costs = Counter(cost)
    for x in costs.keys():
        costAux = costs
        costAux[x] -= 1
        y = money - x
        if costAux[y] > 0:
            i = cost.index(x) + 1
            j = cost.index(y, i) + 1
            print(f"{i} {j}")
            return
