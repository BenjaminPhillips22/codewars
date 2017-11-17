# https://www.codewars.com/kata/5541f58a944b85ce6d00006a

# %%


def productFib(prod):
    f1 = 1
    f2 = 1
    while(True):
        if f1*f2 == prod:
            return([f1, f2, True])
        if f1*f2 > prod:
            return([f1, f2, False])
        f2 = f1 + f2
        f1 = f2 - f1


# %%

# tests

print(productFib(4895))
print(productFib(4895) == [55, 89, True])

print(productFib(5895) == [89, 144, False])
print(productFib(5895))
