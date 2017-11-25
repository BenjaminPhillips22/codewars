# https://www.codewars.com/kata/pi-approximation

# %%

import numpy as np


def iter_pi(epsilon):
    i = 0
    series_sum = 0
    while True:
        series_sum += 1/(((-1)**i)*(i*2+1))
        if abs(4*series_sum-np.pi) < epsilon:
            return [i+1, round(4*series_sum, 10)]
        i += 1


# %%

# tests

print(iter_pi(0.1))
print(iter_pi(0.01))

# %%

# other solutions
# I like this one for it's readability

from math import pi


def iter_pi(epsilon):
    my_pi = 0
    n = sign = 1
    
    while epsilon < abs(pi - my_pi):
        my_pi += 4.0 / n * sign
        n += 2
        sign *= -1
    
    return [n//2, round(my_pi, 10)]
