km = float(input('Digite a quantidade de quilometros rodados: '))
d = int(input('Digite a quantidade de dias que ele foi alugado: '))

vKm = km * 0.15
vD = d * 60
t = vKm + vD

print('Valor de km rodados = {:.2f} \nValor de dias alugados = {:.2f} \nTotal = {:.2f}'.format(vKm, vD, t))
