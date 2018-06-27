# https://www.codewars.com/kata/replace-with-alphabet-position

# %% 


def alphabet_position(text):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    alphabet_dict = {
        letter: number for letter, number in zip(alphabet, range(1, 27))
    }

    text_clean = [letter for letter in text.lower() if letter in alphabet]

    positions = ' '.join([str(alphabet_dict[letter]) for letter in text_clean])

    return positions

# %%


print(alphabet_position('hi Ben 234'))

# %%

# Other solutions


def alphabet_position(text):
    return ' '.join(str(ord(c) - ord('a') + 1) for c in text.lower() if c.isalpha())
