from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("JOKENPO")
jogador = int(input("[0] Pedra\n"
                    "[1] Papel\n"
                    "[2] Tesoura\n\n"
                    "Digite o valor que deseja jogar: "))
print("-="*11)
print("Jogador jogou {}".format(itens[jogador]))
print("Computador jogou {}".format(itens[computador]))
print("-="*11)
if computador == 0:
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("Jogador ganhou!")
    elif jogador == 2:
        print("Computador ganhou")
    else:
        print('Jogada Invalida')
elif computador == 1:
    if jogador == 0:
        print("Computador ganhou")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
        print("Jogador Ganhou")
    else:
        print('Jogada Invalida')
else:
    if jogador == 0:
        print("Jogador ganhou")
    elif jogador == 1:
        print("Computador ganhou")
    elif jogador == 2:
        print("Empate")
    else:
        print('Jogada Invalida')