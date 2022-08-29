import moeda

valor = float(input('Digite o valor R$'))

print(f'A metade de R${valor:.2f} é R${moeda.metade(valor):.2f}')
print(f'O dobro de R${valor:.2f} é R${moeda.dobro(valor):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(10, valor):.2f}')