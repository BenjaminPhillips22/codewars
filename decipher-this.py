# https://www.codewars.com/kata/decipher-this


def get_chr(word):
    return chr(int(''.join([s for s in word if s.isdigit()])))


def swap_letters(word):
    if len(word) <= 1:
        return word
    return word[-1] + word[1:-1] + word[0]


def decipher_this(string):
    first_letter = [get_chr(word) for word in string.split(' ')]
    unswitched_words = ''.join([s for s in string if not s.isdigit()]).split(' ')
    switched_words = [swap_letters(word) for word in unswitched_words]
    words = [l+w for l, w in zip(first_letter, switched_words)]
    return ' '.join(words)


# tests

print(get_chr('65tt'))
print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))

print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka") == "A wise old owl lived in an oak")
print(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp") == "The more he saw the less he spoke")
print(decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare") == "The less he spoke the more he heard")
print(decipher_this("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri") == "Why can we not all be like that wise old bird")
print(decipher_this("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple") == "Thank you Piotr for all your help")


# other solutions


def decipher_word(word):
    i = sum(map(str.isdigit, word))
    decoded = chr(int(word[:i]))
    if len(word) > i + 1:
        decoded += word[-1]
    if len(word) > i:
        decoded += word[i+1:-1] + word[i:i+1]
    return decoded


def decipher_this(string):
    return ' '.join(map(decipher_word, string.split()))