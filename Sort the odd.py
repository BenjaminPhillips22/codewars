"""
https://www.codewars.com/kata/sort-the-odd
You have an array of numbers.
Your task is to sort ascending odd numbers
but even numbers must be on their places.
Zero isn't an odd number and you don't
need to move it. If you have an empty array,
you need to return it.
"""

# %%
import numpy as np


def sort_array(source_array):
    if not source_array:
        return source_array

    sa = np.array(source_array)
    even_mask = np.ma.masked_where(sa % 2 == 0, sa)
    return even_mask


# %%

# tests

print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4])
