n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
p = n1 ** n2

print('Soma = {} \nSubtração = {} \nMultiplicação = {} \nPotencia = {} '.format(s, sub, m, p))
print('Divisão = {} \nDivisão inteira = {} \nResto da Divisão = {}'.format(d, di, r));