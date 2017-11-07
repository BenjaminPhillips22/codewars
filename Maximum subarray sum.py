"""
Maximum subarray sum
The maximum sum subarray problem consists
in finding the maximum sum of a contiguous
subsequence in an array or list of integers:
"""

# %%


def maxSequence(arr):
    return max([
                sum(arr[start:end])
                for start in range(len(arr))
                for end in range(len(arr))
                if sum(arr[start:end]) >= 0
            ], default=0)


# %%

# tests
print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(maxSequence([]) == 0)
print(maxSequence([-1, -2, -3]) == 0)
