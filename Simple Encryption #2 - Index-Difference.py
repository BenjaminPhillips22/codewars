"""
https://www.codewars.com/kata/simple-encryption-number-2-index-difference
You are given two arrays a1 and a2 of strings.
Each string is composed with letters from a to z.
Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))
"""

# %%


def mxdiflg(a1, a2):
    a1_len = [len(i) for i ing a1]
    return a1_len







# %%

# tests

s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis",
      "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2) == 13)
