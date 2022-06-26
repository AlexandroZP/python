menorP = 0
maiorP = 0
for c in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    if c == 1:
        maiorP = peso
        menorP = peso
    else:
        if peso > maiorP:
            maiorP = peso
        if peso < menorP:
            menorP = peso
print('O maior peso lido foi de {}Kg'
      '\nO menor peso lido foi de {}Kg'.format(maiorP, menorP))
