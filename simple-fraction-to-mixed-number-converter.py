# https://www.codewars.com/kata/simple-fraction-to-mixed-number-converter

# %%


def mixed_fraction(s):
    return None


# %%

# tests

mixed_fraction()
print(mixed_fraction('42/9'))
print(mixed_fraction('-10/7'))

print(mixed_fraction('42/9') == '4 2/3')
print(mixed_fraction('6/3') == '2')
print(mixed_fraction('4/6') == '2/3')
print(mixed_fraction('0/18891') == '0')
print(mixed_fraction('-10/7') == '-1 3/7')
print(mixed_fraction('-22/-7') == '3 1/7')
