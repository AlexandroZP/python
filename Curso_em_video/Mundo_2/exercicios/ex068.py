from random import randint

vitorias = 0

while True:
    print('=-' * 20)

    player = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PpiI':
        pi = str(input('Par ou Ímpar ? [P/I]')).upper().strip()[0]
    
    print('-' * 20)

    c = randint(0, 10)
    t = player + c

    print(f'Você jogou {player} e o computador {c}.')
    print('-' * 20)

    if pi == 'P':
        if t % 2  == 0:
            print('Você venceu!!')
            vitorias += 1
        else:
            print('Você perdeu!!')
            break
    elif pi == 'I':
        if t % 2 != 0:
            print('Você venceu!!')
            vitorias += 1
        else:
            print('Você perdeu!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitorias} vezes')
        


    