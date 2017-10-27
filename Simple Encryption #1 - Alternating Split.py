"""
For building the encrypted string:
Take every 2nd char from the string,
then the other chars, that are not every 2nd char,
and concat them as new String.
Do this n times!
"""

# %%


def decrypt(encrypted_text, n):
    pass


def encrypt(text, n):
    pass


# %%

# tests

print(encrypt("This is a test!", 1) == "hsi  etTi sats!")
print(decrypt("Thsi  etTi sats!", 1) == "This is a test!")
