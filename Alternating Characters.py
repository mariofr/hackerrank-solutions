# https://www.hackerrank.com/challenges/alternating-characters/problem

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    dels = 0
    lastChar = None
    for x in s:
        if x != lastChar:
            lastChar = x
        else:
            dels += 1
    return dels
	