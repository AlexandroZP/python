qt = s = ma = mn = 0
r = 'S'
while r == 'S':
    qt += 1
    n = int(input('Digite um número: '))
    s += n
    if qt == 1:
        ma = mn = n
    else:
        if ma < n:
            ma = n
        if mn > n:
            mn = n
    r = str(input('Quer continuar ? [S/N] ')).upper().strip()
print('O maior número é {} e o menor número é {}. A média entre os números é {}'.format(ma, mn, s/qt))
