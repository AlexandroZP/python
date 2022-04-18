r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2+r3 and r2 < r3+r1 and r3 < r1+r1:
    print('As três retas formam um triângulo!')
else:
    print('As retas não formam um triângulo!')
