# https://www.codewars.com/kata/maximum-subarray-sum


def maxSequence(arr):
    best = cur = 0
    for i in arr:
        cur = max(cur + i, 0)
        best = max(best, cur)
    return best


# test

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
