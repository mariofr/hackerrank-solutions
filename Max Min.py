# https://www.hackerrank.com/challenges/angry-children/problem

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    if k >= len(arr):
        return arr[-1] - arr[0]
    unfair = float('inf')
    for i, x in enumerate(arr[:-k+1]):
        un = arr[i+k-1] - x
        if un < unfair:
            unfair = un
    return unfair
    