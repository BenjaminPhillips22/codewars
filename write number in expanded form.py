# https://www.codewars.com/kata/write-number-in-expanded-form

# %%


def expanded_form(num):
    t = [l + '0'*(len(str(num))-i-1) for i, l in enumerate(str(num)) if l != '0']
    return ' + '.join(t)


# %%

# tests

print(expanded_form(12))
print(expanded_form(70304))
