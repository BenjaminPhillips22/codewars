# https://www.codewars.com/kata/lambdas-as-a-mechanism-for-open-slash-closed

spoken    = lambda greeting: greeting.capitalize()+'.'
shouted   = lambda greeting: greeting.upper()+'!'
whispered = lambda greeting: greeting.lower()+'.'

greet = lambda style, msg: style(msg)

print(greet(style=shouted, msg='goodness gracious'))


def plus_one(num):
    return num + 1


def squared(num):
    return num*num


def do_thing(func, num):
    return func(num)


print(do_thing(plus_one, 2))

print(do_thing(squared, 2))
