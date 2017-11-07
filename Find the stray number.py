"""
Find the stray number
You are given an odd-length array of integers,
in which all of them are the same,
except for one single number.
"""

# %%


def stray(arr):
    return [i for i in arr if arr.count(i) == 1][0]


# %%

# tests

a = [1, 1, 3, 1, 1]
b = [3, 4, 4, 4, 4]
print(stray(a))
print(stray(b))

# Other solutions
# (https://www.codewars.com/users/EDjur)


def stray(arr):
    return min(arr, key=arr.count)
