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


def sort_array(source_array):
    odds = sorted([x for x in source_array if x % 2 != 0], reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]


# %%

# tests
print(sort_array([5, 3, 2, 8, 1, 4]))
