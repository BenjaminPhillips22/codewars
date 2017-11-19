# https://www.codewars.com/kata/reverse-words

# %%


def reverse_words(str):
    return ' '.join([s[::-1] for s in str.split(sep=' ')])


# %%

# tests

print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))
print(reverse_words("An example!") == "nA !elpmaxe")
print(reverse_words("double  spaces") == "elbuod  secaps")
print(reverse_words("This is an example!") == "sihT si na !elpmaxe")
