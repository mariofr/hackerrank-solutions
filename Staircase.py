# https://www.hackerrank.com/challenges/staircase/problem

# Complete the staircase function below.
def staircase(n):
    x = n - 1
    while x >= 0:
        print(x*" " + (n-x)*"#")
        x -= 1