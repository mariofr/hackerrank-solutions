# https://www.hackerrank.com/challenges/two-strings/problem

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    a = set(s1)
    b = set(s2)
    return "YES" if a.intersection(b) else "NO"
	