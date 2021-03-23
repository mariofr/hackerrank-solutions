# https://www.hackerrank.com/challenges/marcs-cakewalk/problem

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    miles = 0
    for i, cake in enumerate(calorie):
        miles += (2 ** i) * cake
    return miles