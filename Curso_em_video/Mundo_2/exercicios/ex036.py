valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quanto anos pretendo pagar: '))
minimo = salario * 0.30
prestação = valor_casa / (anos * 12)
print('\033[1;37m=\033[m'*40)
print('Para pagar uma casa de \033[1:34mR${:.2f}\033[m em {} anos, \nAs prestações seriam \033[1:34mR${:.2f}\033[m'.format(valor_casa, anos, prestação))
print('\033[1;37m#\033[m'*40)
if minimo >= prestação:
    print('\033[:32mEmpréstimo aprovado!\033[m')
else:
    print('\033[:31mEmprestimo recusado! Você não possui os requistos necessários para esta transação.\033[m')
