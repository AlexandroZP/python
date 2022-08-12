from random import randint
from time import sleep as slp
from operator import itemgetter as itg # Pega o item selecionado (0 ou 1) key ou valor de um dicionario
jogadores = {
    'Jogador 1':randint(1, 6),
    'Jogador 2':randint(1, 6),
    'Jogador 3':randint(1, 6),
    'Jogador 4':randint(1, 6)
}
ranking = []
print('Jogando os dados...')
for jogador, dado in jogadores.items():
    slp(1.5)
    print(f'{jogador} tirou {dado}')
ranking = sorted(jogadores.items(), key=itg(1), reverse=True) # Ordena baseado no valor(key=itg(1)) 'Os valores dos dicionarios'

for index, valor in enumerate(ranking):
    print(f'{index+1}° Lugar: {valor[0]}  com o valor: {valor[1]} no dado.')
    slp(1)