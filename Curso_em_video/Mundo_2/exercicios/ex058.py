from random import randint
print('Sou seu computador...')
comp = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10 ')
print('Consegue advinhar ? ')
acertou = False
palps = 0

while not acertou:
    palp = int(input('Qual é seu palpite ? '))
    palps += 1
    if palp == comp:
        acertou = True
    else:
        if palp > comp:
            print('Menos..tente novamente.')
        else:
            print('Mais...tente novamente.')
print('O número era {}. Você acertou em {}, parábens!!'.format(comp, palps))

