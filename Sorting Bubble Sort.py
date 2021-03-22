# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for x in a:
        for i, x in enumerate(a[:-1]):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps += 1
    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
