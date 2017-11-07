"""
https://www.codewars.com/kata/simple-encryption-number-2-index-difference
You are given two arrays a1 and a2 of strings.
Each string is composed with letters from a to z.
Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))
"""

# %%


def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1

    return max([len(sorted(a1, key=len)[-1]) -
                len(sorted(a2, key=len)[0]),
                len(sorted(a2, key=len)[-1]) -
                len(sorted(a1, key=len)[0])])


# %%

# tests

s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis",
      "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2) == 13)

# %%

# other solutions
# (https://www.codewars.com/users/biskinis)


def mxdiflg(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1
