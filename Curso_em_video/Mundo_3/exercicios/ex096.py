def calc_area(larg, comp):
    area = larg * comp
    return area


print('----- Controle de terronos ------')
print('-' * 40)
largura = float(input('LARGURA: '))
comprimento = float(input('COMPRIMENTO: '))

print(f'A área de um terreno {largura} x {comprimento} é de {calc_area(largura, comprimento)}m².')