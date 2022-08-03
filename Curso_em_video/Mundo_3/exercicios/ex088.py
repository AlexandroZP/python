from random import randint
from time import sleep as slp


print('-=' * 40)
print('MEGA SENA!!!')
print('-=' * 40)

qtd_jogos = int(input('Quantos jogos você quer que eu sorteie ? '))
jogos = []

for c in range(0, qtd_jogos):
    jogo = []
    for i in range(0, 6):
        jogo.append(randint(1, 60))
        jogo.sort()
    jogos.append(jogo[:])
    print(f'Jogo {c+1}: {jogos[c]}')
    slp(1.25)


print('-='*20, '< BOA SORTE >', '-=' * 20)