# https://www.codewars.com/kata/reverse-words

# %%

def reverse_words(str):
    return str[::-1]



# %%

# tests

print(reverse_words("This is an example!"))
print(reverseWords("An example!") == "nA !elpmaxe")
print(reverseWords "double  spaces" == "elbuod  secaps")
print(reverse_words("This is an example!") == "sihT si na !elpmaxe")
