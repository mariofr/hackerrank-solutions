# https://www.hackerrank.com/challenges/sparse-arrays/problem

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    results = list()
    for q in queries:
        matches = 0
        for s in strings:
            if q == s:
                matches += 1
        results.append(matches)
    return results
