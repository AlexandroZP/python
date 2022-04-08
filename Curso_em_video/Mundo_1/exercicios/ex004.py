n = input('Digite algo: ')

print('O tipo da variavel n é: ', type(n))
print('{} é númerico: '.format(n), n.isnumeric())
print('{} é alphabetico: '.format(n), n.isalpha())
print('{} é alphanumerico'.format(n), n.isalnum())
print('{} So contém letras maiúsculas ?'.format(n), n.isupper())
print('{} só contém letras minúsculas ?'.format(n), n.islower())
print('{} contém maiúsculas e minúsculas ?'.format(n), n.istitle())