def ficha(nome='None', gols=0):
    print('-' * 40)
    jogador = {'Nome':nome, 'Gols':gols}
    print(f'Nome: {jogador["Nome"]}')
    print(f'Gols: {jogador["Gols"]}')


n = str(input('Digite nome do Jogador: '))
g = str(input('Gols marcados: '))

if g.isnumeric():
    g = int(g)
else:
    g=0

if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n, g)