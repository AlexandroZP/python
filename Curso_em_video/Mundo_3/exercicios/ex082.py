valores = []
valores_impares = []
valores_pares = []

while True:
    valor = int(input('Digite um número: '))
    valores.append(valor)
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)
    s_n = str(input('Quer continuar ? [S/N] ')).upper().split()[0]
    if s_n == 'N':
        break

print(f'A lista completa é {valores}.')
print(f'A lista de pares é {valores_pares}.')
print(f'A lista de impares é {valores_impares}.')