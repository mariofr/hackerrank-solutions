# https://www.hackerrank.com/challenges/jim-and-the-orders/problem

# Complete the jimOrders function below.
def jimOrders(orders):
    times = list()
    x = 1
    for a, b in orders:
        times.append((a+b, x))
        x += 1
    times.sort()
    result = list()
    for a, b in times:
        result.append(b)
    return result
