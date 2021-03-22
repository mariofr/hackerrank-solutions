# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import bisect
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort()
	# Binary search for the first tallest candle
    i = bisect.bisect_left(candles, candles[-1])
    return len(candles) - i