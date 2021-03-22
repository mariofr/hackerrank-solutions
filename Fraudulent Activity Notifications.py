# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

import bisect
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifs = 0
    prevdays = list(expenditure[:d])
    prevdays.sort()
    for i, x in enumerate(expenditure[d:], d):
        if i != d:
            ##prevdays.remove(expenditure[i-d])
            del prevdays[bisect.bisect_left(prevdays, expenditure[i-d-1])]
            bisect.insort_left(prevdays, expenditure[i-1])
        if d % 2 == 0:
            med = prevdays[d//2 - 1] + prevdays[d//2]
        else:
            med = prevdays[d//2] * 2
        if x >= med:
            notifs += 1
    return notifs