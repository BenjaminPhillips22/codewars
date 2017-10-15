# https://www.codewars.com/kata/sum-of-two-lowest-positive-integers

# %%


def sum_two_smallest_numbers(numbers):
    numbers.sort(key=lambda x: x if x > 0 else 1e100)
    return sum(numbers[:2])

# %%

# test


print("?")
print(sum_two_smallest_numbers([-3, -5, 0, -2, 1, 2, 5]))
print(sum_two_smallest_numbers(
      [10, 343445353, 3453445, 3453545353453]))

# %%
sorted([10, 343445353, 3453445, 3453545353453])
assert (sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13), "didn't passed"
print(10 % 1)