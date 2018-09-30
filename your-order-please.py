# https://www.codewars.com/kata/your-order-please

import re


def order(sentence):
    return ' '.join(sorted(sentence.split(' '), key=lambda x: int(re.findall('\d+', x)[0])))


# Tests

print(order("is2 Thi1s T4est 3a"))
print(order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est")
