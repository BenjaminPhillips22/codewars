# https://www.codewars.com/kata/write-number-in-expanded-form-part-2

# %%


def expanded_form(num):
    upper, lower = str(num).split(sep='.')
    upper = [l + '0'*(len(upper)-i-1) for i, l in enumerate(upper) if l != '0']
    lower = [l + '/1' + '0'*(i+1) for i, l in enumerate(lower) if l != '0']
    return ' + '.join([' + '.join(out) for out in [upper, lower] if out != []])


# %%

# tests


print(expanded_form(1.24))
print(expanded_form(1234.5678))
print(expanded_form(0.03))
print(expanded_form(1.24) == '1 + 2/10 + 4/100')
print(expanded_form(7.304) == '7 + 3/10 + 4/1000')
print(expanded_form(807.304) == '800 + 7 + 3/10 + 4/1000')
