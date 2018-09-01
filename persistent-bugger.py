# https://www.codewars.com/kata/persistent-bugger

import numpy as np


def persistence(n):
    p = 0
    while(True):
        if n < 10:
            return p
        p += 1
        n = np.prod(list(map(int, list(str(n)))))


# tests

print(persistence(112))
print(persistence(39) == 3)
print(persistence(4) == 0)
print(persistence(25) == 2)
print(persistence(999) == 4)

# Other Solutions

from operator import mul
def persistence(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1
