# https://www.codewars.com/kata/unary-function-chainer


def chained(functions):
    def chain(input):
        for f in functions:
            input = f(input)
        return input
    return chain


# tests


def add_a(letter):
    return letter + ' a'


def add_b(letter):
    return letter + ' b'


print(chained([add_a, add_b])('1'))
