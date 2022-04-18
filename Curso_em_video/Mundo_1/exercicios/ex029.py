velocidade = float(input('A que velocidade seu carro está ? '))

if velocidade > 80.0:
    multa = (velocidade-80.0)*7.00
    print('Você ultrapassou o limete de velocidade, a multa irá custar R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia e dirija com cuidado!')
