# https://www.codewars.com/kata/two-sum


def two_sum(numbers, target):
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i != j and x + y == target:
                return [i, j]


# test
print(two_sum([1, 2, 3, 4], 5))
