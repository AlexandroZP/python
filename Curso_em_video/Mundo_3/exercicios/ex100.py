from random import randint
from time import sleep as slp


def sorteando(qtd, val):
    for c in range(0, qtd):
        val.append(randint(0, 10))


def somando_par(val):
    soma = 0
    for c in val:
        if c % 2 == 0:
            soma += c
    return soma


# Programa principal
q_valores = randint(0, 10)
valores = []

print(f'Sorteando {q_valores} valores')
sorteando(q_valores, valores)


for valor in valores:
    print(valor, end=' ', flush=True)
    slp(0.55)


print('PRONTO!!')
print(f'\nSomando os valores pares de {valores}, temos {somando_par(valores)}')