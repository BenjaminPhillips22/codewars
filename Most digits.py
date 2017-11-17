# https://www.codewars.com/kata/most-digits/train/python

# %%


def find_longest(arr):
    return int(sorted([str(i) for i in arr], key=len, reverse=True)[0])


# tests

print(find_longest([1, 10, 100, 101]))
print(find_longest([1, 10, 100]) == 100)
print(find_longest([9000, 8, 800]) == 9000)

# %%

# other solutions


def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))
