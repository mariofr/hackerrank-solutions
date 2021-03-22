# https://www.hackerrank.com/challenges/2d-array/problem

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = float('-inf')
    for y in range(4):
        for x in range(4):
            hour_sum = arr[y][x] + arr[y][x+1] + arr[y][x+2] + arr[y+1][x+1] + arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]
            if hour_sum > max_sum:
                max_sum = hour_sum
    return max_sum
