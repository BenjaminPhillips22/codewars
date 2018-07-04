# http://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie


def namelist(names):
    if len(names) == 1:
        return names[0]['name']
    else:
        return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']


# tests
our_names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
print(namelist(our_names))

our_names = [{'name': 'Bart'}]
print(namelist(our_names))
