# https://www.hackerrank.com/challenges/sock-merchant/problem

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = dict()
    result = 0
    for x in ar:
        if x in pairs:
            pairs[x] += 1
        else:
            pairs[x] = 1
    for x in pairs.values():
        result += x // 2
    return result