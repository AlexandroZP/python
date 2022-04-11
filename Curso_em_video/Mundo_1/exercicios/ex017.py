from math import hypot

cat_op = float(input('Digite o cateto oposto do triângulo: '))
cat_adj = float(input('Digite o cateto adjacente do triângulo: '))

hipt = (cat_op ** 2 + cat_adj ** 2)**0.5
hipt_2 = hypot(cat_op, cat_adj)
print('O Cateto oposto é {} e o adjacente é {} o comprimento da hipotenusa é {}'.format(cat_op, cat_adj, hipt))
print('O Cateto oposto é {} e o adjacente é {} o comprimento da hipotenusa é {}'.format(cat_op, cat_adj, hipt_2))