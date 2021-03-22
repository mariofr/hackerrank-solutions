# https://www.hackerrank.com/challenges/luck-balance/problem

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    contests.sort(reverse=True)
    for x in contests:
        if x[1] == 0:
            luck += x[0]
        else:
            if k > 0:
                luck += x[0]
                k -= 1
            else:
                luck -= x[0]
    return luck
    
