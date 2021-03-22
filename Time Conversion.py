# https://www.hackerrank.com/challenges/time-conversion/problem
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2] == "A":
        if s[:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        if s[:2] == "12":
            return s[:-2]
        else:
            s_aux = s.split(":")
            h = int(s_aux[0])
            h += 12
            t = str(h) + ":" + s_aux[1] + ":" + s_aux[2][:2]
            return t
