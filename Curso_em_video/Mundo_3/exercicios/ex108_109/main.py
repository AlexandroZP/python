import moeda

valor = float(input('Digite o valor R$'))

print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(10, valor, True)}')
print(f'diminuindo 13%, temos {moeda.diminuir(13, valor, True)}')