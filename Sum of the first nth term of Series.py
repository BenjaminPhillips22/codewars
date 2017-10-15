# Sum of the first nth term of Series

# %%


def return_as_string(flo):
    if len(str(flo)) == 4:
        return str(flo)
    else:
        return str(flo) + '0'


def series_sum(n):
    # Happy Coding ^_^
    if not n:
        return '0.00'

    aaa = [x for x in range(1, n*3) if (x-1) % 3 == 0]
    bbb = [1/y for y in aaa]

    return return_as_string(round(sum(bbb), 2))


# %%

# tests

print(series_sum(15))
print([series_sum(i) for i in range(20)])

# %%

# Other Clever solutions


def series_sum_v1(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))


print(series_sum_v1(15))
print(series_sum_v1(0))
