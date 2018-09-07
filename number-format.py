# https://www.codewars.com/kata/number-format


def number_format(n):
    return format(n, ',')


# tests

print(number_format(-10))
print(number_format(100000) == "100,000")
print(number_format(5678545) == "5,678,545")
print(number_format(-420902) == "-420,902")
print(number_format(-3) == "-3")
