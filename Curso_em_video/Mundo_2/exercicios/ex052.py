n = int(input('Digite um número: '))
ct = 0
for c in range(1, n+1):
    if n % c == 0:
        ct += 1
        print('\033[033m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m\nO número {} foi divisel {} vezes'.format(n, ct))
if ct > 2:
    print('Por isso não é um número primo')
else:
    print('Por isso é um número primo')
