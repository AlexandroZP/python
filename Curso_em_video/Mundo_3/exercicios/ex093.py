jogador = {}
jogador['Nome'] = str(input('Nome do jogador: '))
n_partidas = int(input('Quantas partidas ele jogou: '))
g_partidas = []

print()
for c in range(0, n_partidas):
    g_partidas.append(int(input(f'      Quantos gols na {c+1}º partida: ')))


jogador['Gols'] = g_partidas[:]
jogador['Total de gols'] = sum(g_partidas)
print('_' * 40)
print(jogador)
print('-=' * 40)
for chave, valor in jogador.items():
    print(f'{chave}: {valor} ')
print('-=' * 40)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas\n')
for partida, gols in enumerate(jogador['Gols']):
    print(f'    Na {partida+1}º partida marcou {gols} gols.')
print(f'Total de Gols: {jogador["Total de gols"]}')
