# https://www.hackerrank.com/challenges/drawing-book/problem
#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
	# Get nearest even page
    if p % 2 == 1:
        p = p - 1
    if n % 2 == 1:
        n = n - 1
    if n == p:
        return 0
    begin = p // 2
    end = (n-p) // 2
    return min(begin, end)