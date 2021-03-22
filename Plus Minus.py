# https://www.hackerrank.com/challenges/plus-minus/problem

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1
    print(f"{pos/len(arr):.6f}")
    print(f"{neg/len(arr):.6f}")
    print(f"{zero/len(arr):.6f}")
	