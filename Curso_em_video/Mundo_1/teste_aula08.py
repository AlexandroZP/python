import random
from math import sqrt, floor
import emoji
num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

num_2 = random.randint(1, 10)
print(num_2)