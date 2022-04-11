from cmath import cos
from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(an))
con = cos(radians(an))
tang = tan(radians(an))
print('O ângulo de {} \nTem o SENO de {} \nTem o COSSENO de {} \nTem a tangente de{}'.format(an, sen, con, tang))