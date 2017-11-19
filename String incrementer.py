# https://www.codewars.com/kata/string-incrementer

# %%
import re


def increment_string(strng):
    a = re.findall(pattern=r'[0-9]+', string=strng)
    b = [str(j) for j in [1 if i == [] else int(i) for i in a]]
    return b


# %%

# tests

print(increment_string("foo"))
print(increment_string("foo") == "foo1")
print(increment_string("foobar001"))
print(increment_string("foobar001") == "foobar002")
print(increment_string("foobar1") == "foobar2")
print(increment_string("foobar00") == "foobar01")
print(increment_string("foobar99") == "foobar100")
print(increment_string("foobar099") == "foobar100")
