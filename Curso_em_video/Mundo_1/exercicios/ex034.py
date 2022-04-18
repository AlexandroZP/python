salario = float(input('Digite seu salário: '))

if salario <= 1250.00:
    pAumento = 15
    aumento = salario * 0.15
    nsalario = salario + aumento
else:
    pAumento = 10
    aumento = salario * 0.10
    nsalario = salario + aumento

print('O salario atual é R${:.2f}, o aumento dado foi de {}%(R${:.2f}), novo salario R${:.2f}'.format(salario, pAumento, aumento, nsalario))