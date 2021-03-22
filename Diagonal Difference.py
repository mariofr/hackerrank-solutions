# https://www.hackerrank.com/challenges/diagonal-difference/problem
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diag1 = 0
    diag2 = 0
    for x in range(len(arr)):
        diag1 += arr[x][x]
        diag2 += arr[len(arr)-1-x][x]
    return abs(diag1 - diag2)