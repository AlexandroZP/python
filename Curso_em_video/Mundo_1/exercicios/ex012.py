preço = float(input('Digite o preço do produto: R$'))

d = preço * 0.05
vD = preço - d

print('Valor original R${:.2f}, desconto de 5% é igual à R${:.2f}, seu novo preço é R${:.2f}'.format(preço, d, vD))