# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dic = dict()
    for x in magazine:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    for x in note:
        if x in dic:
            dic[x] -= 1
            if dic[x] == 0:
                dic.pop(x)
        else:
            print("No")
            return
    print("Yes")
    return
