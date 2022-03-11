import itertools

str = input('Palavra a ser permutada: ')

resultado = itertools.permutations(str, len(str))

for x in resultado:
    print(''.join(x))