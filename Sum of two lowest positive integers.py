# https://www.codewars.com/kata/sum-of-two-lowest-positive-integers

# %%


def sum_two_smallest_numbers(numbers):
    numbers.sort(key=lambda x: x if x > 0 else 1e100)
    return sum(numbers[:2])

# %%

# tests


assert (sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13), "didn't pass"
assert (sum_two_smallest_numbers([-3, -5, 0, -2, 1, 2, 5])), "didn't pass"
assert (sum_two_smallest_numbers(
      [10, 343445353, 3453445, 3453545353453])), "didn't pass"
