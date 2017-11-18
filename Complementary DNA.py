# https://www.codewars.com/kata/complementary-dna

# %%


def DNA_strand(dna):
    transforms = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([transforms[t] for t in dna])


# %%

# tests

print(DNA_strand("AAAA"))
print(DNA_strand("AAAA") == "TTTT")
print(DNA_strand("ATTGC") == "TAACG")
