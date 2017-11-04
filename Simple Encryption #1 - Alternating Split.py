"""
https://www.codewars.com/kata/simple-encryption-number-1-alternating-split
For building the encrypted string:
Take every 2nd char from the string,
then the other chars, that are not every 2nd char,
and concat them as new String.
Do this n times!
"""

# %%


def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    for i in range(n+1, n+100):
        if encrypted_text == encrypt(encrypted_text, i):
            ma = i
            break
    return encrypt(encrypted_text, ma-n)


def encrypt(text, n):
    if not text or n <= 0:
        return text

    if n == 1:
        return text[1::2] + text[::2]
    else:
        return encrypt(text[1::2] + text[::2], n-1)


# %%

# some tests

print(encrypt("This is a test!", 1) == "hsi  etTi sats!")
print(decrypt("hsi  etTi sats!", 1) == "This is a test!")

# %%

# Other Solutions
# (https://www.codewars.com/users/Blind4Basics)

text = 'hsi  etTi sats!'
decodeList = encrypt(list(range(len(text))),1)
print(decodeList)
b = [decodeList.index(i) for i in range(len(text))]
print(b)

def decrypt(text, n):
    if text == None: return text
    
    decodeList = encrypt(list(range(len(text))),n)
    return ''.join( text[decodeList.index(i)] for i in range(len(text)) )


def encrypt(text, n):
    if text == None: return text
    return encrypt(text[1::2] + text[0::2],n-1) if n>0 else text


print(encrypt("This is a test!", 1) == "hsi  etTi sats!")
print(decrypt("hsi  etTi sats!", 1) == "This is a test!")
