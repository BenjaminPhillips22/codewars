# https://www.codewars.com/kata/highest-scoring-word


def high(x):
    words = x.split(sep=" ")
    word_score = list()
    for word in words:
        word_score.append(sum([ord(letter)-96 for letter in word]))
    return words[word_score.index(max(word_score))]


# tests

print(high('man i need a taxi up to ubud') == 'taxi')

# other solutions


def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
