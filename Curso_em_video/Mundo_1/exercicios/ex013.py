salario = float(input('Digite seu salário: R$'))

aumento = salario * 0.15
nSalario = salario + aumento

print('Antigo salario R${:.2f}, aumento recebido de R${:.2f}(15%), novo salário R${:.2f}'.format(salario, aumento, nSalario))