from random import randint

valores = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
maior = menor = 0
print('Valores sorteados foram: ', end='')
for valor in valores:
    print(f'{valor} ', end='')

print(f'\nO maior valor foi {max(valores)}') # A função max() retorna o maior valor de uma tupla/lista
print(f'O menor valor foi {min(valores)}') # A função min() retorna o menor valor de uma tupla/lista
