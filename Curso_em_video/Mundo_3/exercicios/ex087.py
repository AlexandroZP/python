valores = [
        [], 
        [],
        []
        ]
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{l}][{c}]: '))
        valores[l].append(valor)

print('-=' * 40)
for l in range(0, len(valores)):
    for valor in valores[l]:
        print(f'[ {valor:^5} ]', end=' ')
    print()

par = soma_3 = maiorS = 0
for l in range(0, len(valores)):
    for valor in valores[l]:
        if valor % 2 == 0:
            par += valor
    soma_3 += valores[l][2]
for c in range(0, len(valores)):
    if c == 0 or valores[1][c] > maiorS:            
        maiorS = valores[1][c]
print('-=' *40)
print(f'\nA soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna é: {soma_3}')
print(f'O maior valor da segunda linha é: {maiorS}')