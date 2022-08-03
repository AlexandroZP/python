pessoas = []

while True:
    pessoa = []
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    s_n = str(input('Deseja continuar ? [S/N] ')).upper().split()[0]

    if s_n in 'nN':
        break

maiores = []
menores = []
for indice, pessoa in enumerate(pessoas):
    if indice == 0:
        maiores.append(pessoa[:])
        menores.append(pessoa[:])    
    else:
        if pessoa[1] ==  maiores[0][1]:
            maiores.append(pessoa[:])
        elif pessoa[1] > maiores[0] [1]:
            maiores.clear()
            maiores.append(pessoa[:])

        if pessoa[1] == menores[0][1]:
            menores.append(pessoa[:])
        elif pessoa[1] < menores[0][1]:
            menores.clear()
            menores.append(pessoa[:])

print(f'O total de pessoas cadastradas {len(pessoas)}')
print(f'O maior peso foi de {maiores[0][1]}Kg. Peso de ', end='')

for pessoa in maiores:
        print(f'[{pessoa[0]}]', end=' ')

print(f'\nO menor peso foi de {menores[0][1]}Kg. Peso de ', end='')

for pessoa in menores:
        print(f'[{pessoa[0]}]', end=' ')

    

    

