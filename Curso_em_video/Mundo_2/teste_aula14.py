'''for c in range(1, 10):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''
n = 1
r = 'S'
'''while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar ? [S/N] ').upper().strip())
print('Fim')'''

n = 1
p = i = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1
print('A quantidade de números pares é {}.'
      '\nA quantidade de números impares é {}.'.format(p, i))
print('Acabou!!')

