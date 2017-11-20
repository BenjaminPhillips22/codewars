# https://www.codewars.com/kata/string-incrementer

# %%
import re


def increment_string(strng):
    nums = re.findall(pattern=r'[0-9]+', string=strng)
    chars = re.findall(pattern="[a-zA-Z]+", string=strng)
    if nums == []:
        nums.append('0')
    if chars == []:
        chars.append('')
    real_num = int(nums[0]) + 1
    return ''.join([chars[0],
                    '0'*(len(str(nums[0]))-len(str(real_num))),
                    str(real_num)
                    ])


# %%

# tests

print(increment_string("foo"))
print(increment_string("foo") == "foo1")
print(increment_string("foobar0044"))
print(increment_string("foobar001"))
print(increment_string("foobar001") == "foobar002")
print(increment_string("foobar1") == "foobar2")
print(increment_string("foobar00") == "foobar01")
print(increment_string("foobar99") == "foobar100")
print(increment_string("foobar099") == "foobar100")
print(increment_string("foobar099"))
print(increment_string("") == "1")

# %%

# other solutions


def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
