soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o valor {} :'.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
if soma % 2 == 0:
    print('Números imparés: {}. A soma dos valores solicitados é: {}'.format(cont, soma))
