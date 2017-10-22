"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

# %%
import numpy as np


def find_it(seq):
    ar, counts = np.lib.arraysetops.unique(ar=seq,
                                           return_counts=True)
    mask = counts % 2 == 0
    sol = ar[~mask]
    return sol


# %%

# tests

print(find_it([2, 2, 3, 3, 4]))

# %%

# other solutions


def find_it_v1(seq):
    return [x for x in seq if seq.count(x) % 2][0]


print(find_it_v1([2, 2, 3, 3, 4]))
