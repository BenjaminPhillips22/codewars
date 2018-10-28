# https://www.codewars.com/kata/lambdas-as-a-mechanism-for-open-slash-closed

spoken    = lambda greeting: greeting.capitalize()+'.'
shouted   = lambda greeting: greeting.upper()+'!'
whispered = lambda greeting: greeting.lower()+'.'

greet = lambda style, msg: style(msg)

print(greet(style=shouted, msg='goodness gracious'))
