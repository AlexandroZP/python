valores = []
menor = maior = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    if valores[c] >= maior:
        maior = valores[c]
    if valores[c] <= menor:
        menor = valores[c]

print(f'Você digitou os valores: ', end='')
for valor in valores:
    print(valor, end=' ')

print(f'\nMaior valor: {maior}, nas posições', end=' ')
for indice, valor in enumerate(valores):      
    if valor == maior:
        print(f'{indice}...', end=' ')
        
print(f'\nMenor valor: {menor}, nas posições', end=' ')
for indice, valor in enumerate(valores):   
    if valor == menor:
        print(f'{indice}...', end=' ')
