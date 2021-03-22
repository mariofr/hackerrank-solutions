# https://www.hackerrank.com/challenges/counting-valleys/problem

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valley = 0
    elev = 0
    invalley = False
    for x in path:
        if x == 'U':
            elev += 1
            if invalley:
                if elev == 0:
                    valley += 1
                    invalley = False
        else:
            elev -= 1
            if not invalley:
                if elev < 0:
                    invalley = True
                    
    return valley
    