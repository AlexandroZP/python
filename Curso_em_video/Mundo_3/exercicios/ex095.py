from time import sleep as slp
from traceback import print_tb


jogadores = []
jogador = {}
while True:
    jogador.clear()
    gols = []
    jogador['Nome'] = str(input('Nome do jogador: '))
    q_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou ? '))
    if q_partidas > 0:
        for partida in range(0, q_partidas):
            gols.append(int(input(f'    Quantos gols {jogador["Nome"]} fez na {partida+1}º partida: ')))
    else:
        gols.append(0)
    jogador['Gols'] = gols[:]
    jogador['Total de Gols'] = sum(gols)
    jogadores.append(jogador.copy())
    while True: 
        s_n = str(input('Deseja continuar ? [S/N] ')).upper().split()[0]
        if s_n in'SN':
            break
    if s_n == 'N':
        break

print('-=' *40)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-' * 40)

for index, j in enumerate(jogadores):
    print(f'{index:>3} ', end='')
    for dado in j.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 40)


while True:
    i_jogador = int(input('Mostrar dados de qual jogador ? (999 para parar)'))

    if i_jogador == 999:
        break

    if 0 <= i_jogador < len(jogadores):
        j = jogadores[i_jogador].copy()
        print(f' --- Levantamento do Jogador {j["Nome"]} --- ')
        for index, gols in enumerate(j["Gols"]):
            print(f'    No jogo {index+1} fez {gols} gol(s)')
    else:
        print('404 Error. Jogador não encontrado!!')
    slp(0.5)
print('Encerrando o programa...')    
slp(1.25)


