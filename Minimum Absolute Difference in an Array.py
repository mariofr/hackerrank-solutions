# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    minDiff = float('inf')
    numbers = sorted(arr)
    for i in range(len(numbers)-1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff == 0:
            return 0
        if diff < minDiff:
            minDiff = diff
    return minDiff
