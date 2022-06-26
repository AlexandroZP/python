from datetime import date
aa = date.today().year
maiorI = 0
menorI = 0
for c in range(1, 8):
    ano = int(input('Em que ano nasceu a {}° pessoa ? '.format(c)))
    if aa - ano >= 21:
        maiorI += 1
    else:
        menorI += 1
print('Ao todo {} pessoas são maiores de idade e {} são menores.'.format(maiorI, menorI))
