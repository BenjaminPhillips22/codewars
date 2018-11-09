# https://www.codewars.com/kata/reverse-every-other-word-in-the-string


def reverse_alternate(string):
    strip_whitespace = [word for word in string.split(' ') if word != '']
    return ' '.join([word[::-1] if (index+1) % 2 == 0 else word for index, word in enumerate(strip_whitespace)])


# tests

print(reverse_alternate("Basic tests"))
print(reverse_alternate("I really hope it works this time..."))
print(reverse_alternate("Did it work?") == "Did ti work?")
print(reverse_alternate("I really hope it works this time...") == "I yllaer hope ti works siht time...")
print(reverse_alternate("Reverse this string, please!") == "Reverse siht string, !esaelp")
print(reverse_alternate("Have a beer") == "Have a beer")
print(reverse_alternate("") == "")

# Other solutions

def reverse_alternate(string):
    return ' '.join(word[::-1] if i%2 != 0 else word for i, word in enumerate(string.split()))
