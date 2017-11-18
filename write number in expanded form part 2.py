# https://www.codewars.com/kata/write-number-in-expanded-form-part-2

# %%


def expanded_form(num):
    t = [l + '/1' + '0'*(i-1) for i, l in enumerate(str(num)) if l != '0' if l != '.' if i != 0]
    if str(num)[0] != 0:
        return str(num)[0] + ' + ' + ' + '.join(t)
    return ' + '.join(t)


# %%

# tests


print(expanded_form(1.24))
print(expanded_form(1.24) == '1 + 2/10 + 4/100')
print(expanded_form(7.304) == '7 + 3/10 + 4/1000')
