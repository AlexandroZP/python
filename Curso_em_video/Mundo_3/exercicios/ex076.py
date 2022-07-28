listagem = ('Lapiz', 1.75,
            'Borracha', 1.50,
            'Tesoura', 5.50,
            'Caneta', 6.50)

for cont in range(0, len(listagem)):
    if cont % 2 == 0:
        print(f'Produto: {listagem[cont]:.<30}', end=' ')
    else:
        print(f'|Preço: R${listagem[cont]:>4.2f}')
        print('=' * 60)