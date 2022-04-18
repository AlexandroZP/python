viagem = float(input('Digite a distância de sua viagem: '))

if viagem <= 200.00:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('A sua viagem custará R${:.2f}'.format(preço))
