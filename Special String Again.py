# https://www.hackerrank.com/challenges/special-palindrome-again/problem

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    for x in range(n): 
        y = x
        while y < n - 1:
            y += 1
            if s[x] == s[y]:
                count += 1
            else:
                if s[x:y] == s[y+1:2*y-x+1]:
                    count += 1
                break

    return count
