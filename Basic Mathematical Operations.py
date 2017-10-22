"""
Your task is to create a function - basic_op().

The function should take three arguments
operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying
the chosen operation.
"""

# %%

def basic_op(operator, value1, value2):
    d = {
        '+':value1+value2,
        '-':value1-value2,
        '*':value1*value2,
        '/':value1/value2,
    }
    return d[operator]


# %%

# test

print(basic_op('-', 10, 12))

# %%

# other solutions

def basic_op_v1(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))


print(basic_op_v1('-', 10, 13))