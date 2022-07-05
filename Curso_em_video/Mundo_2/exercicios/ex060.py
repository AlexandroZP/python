from math import factorial
print('Digite um número para')
n = int(input('Calcular seu fatorial: '))
c = n
c2 = n
fatorial = 1
fatorialF = 1
print('Calculando {}! : '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial)
print('-='*20)
print('Calculando {}! : '.format(n), end='')
for i in range (0, n):
    print('{}'.format(c2), end='')
    print(' x ' if c2 > 1 else ' = ', end='')
    fatorialF *= c2
    c2 -= 1
print(fatorialF)
