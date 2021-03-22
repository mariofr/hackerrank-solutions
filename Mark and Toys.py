# https://www.hackerrank.com/challenges/mark-and-toys/problem

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    maxtoys = 0
    price = 0
    for x in prices:
        price += x
        if price >= k:
            break
        maxtoys += 1
    return maxtoys
