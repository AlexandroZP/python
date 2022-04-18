from random import randint
from time import sleep
n_1 = int(input('Vou pensar num número entre 0 e 5. Tente advinhar \n'))
n_2 = randint(0, 5)
sleep(2)
if n_1 == n_2:
    print('Parabéns você acertou, o número era {}'.format(n_2))
else:
    print('Você chutou o número {} e o número sorteado foi {}, você perdeu!'.format(n_1, n_2))
