# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c) - 1:
        if i == len(c) - 2:
            jumps += 1
            break
        elif c[i+2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps
        