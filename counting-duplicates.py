# Counting Duplicates


def duplicate_count(text):
    return sum([1 for v in {i: text.lower().count(i) for i in text.lower()}.values() if v > 1])


# tests
print(duplicate_count('abcd'))
print(duplicate_count('abca'))
print(duplicate_count('abcabc'))

# other nice solutions


def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])

