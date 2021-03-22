# https://www.hackerrank.com/challenges/repeated-string/problem

# Complete the repeatedString function below.
def repeatedString(s, n):
    result = (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
    return result
    