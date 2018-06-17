# https://www.codewars.com/kata/build-a-pile-of-cubes


# %%
def find_nb(m):

    def calculate_m(n):
        return sum([i**3 for i in range(n+1)])

    for n in range(m):
        if calculate_m(n) == m:
            return n
        if calculate_m(n) > m:
            return -1

# The above is too inefficient

# %%

# I found an easy way to calculate
# 1**3 + 2**3 + .. + n**3


def find_nb(m):

    def calculate_m(n):
        return int (0.5*n*(n+1))**2

    for n in range(m):
        if calculate_m(n) == m:
            return n
        if calculate_m(n) > m:
            return -1


print(find_nb(3))
print(3**3 + 2**3 + 1)

print(find_nb(2022))
print(find_nb(135440716410000))
print(find_nb(1176845085356508100))

# %%

# There are more efficient ways yet

from math import floor, sqrt

def find_nb(m):
    # Used the formula for the sum of cubes: m = (n(n+1)/2)^2
    # Rearranged to find n^2 + n = n(n+1) ~= n^2 ~= 2sqrt(m),
    # so take square root and round down the result.
    n_canidate = int(floor(sqrt(2 * sqrt(m))))
    if (n_canidate * (n_canidate + 1) / 2 )**2 == m:
        return n_canidate
    else:
        return -1

# %%

def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1
