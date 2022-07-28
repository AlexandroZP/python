palavras = ('Carro',
            'Escada',
            'Apartamento',
            'Transito',
            'Condicionador')
vogais = 'aeiou'
for palavra in palavras:
    print(f'\nVogais na palavra \033[32m{palavra.upper()}\033[m são: ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print(f'\033[34m{letra.lower()}\033[m', end=' ')
