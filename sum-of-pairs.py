# https://www.codewars.com/kata/sum-of-pairs


def sum_pairs(ints, s):
    for i in range(1, len(ints)):
        for j in range(i):
            if ints[j] + ints[i] == s:
                return [ints[j], ints[i]]
    return None


# tests

l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]

print("Testing For Sum of Pairs")
print(sum_pairs(l1, 8))
print(sum_pairs(l1, 8) == [1, 7])
print(sum_pairs(l2, -6) == [0, -6])
print(sum_pairs(l3, -7) == None)
print(sum_pairs(l4, 2) == [1, 1])
print(sum_pairs(l5, 10) == [3, 7])
print(sum_pairs(l6, 8) == [4, 4])
print(sum_pairs(l7, 0) == [0, 0])
print(sum_pairs(l8, 10) == [13, -3])

# other solutions


def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
