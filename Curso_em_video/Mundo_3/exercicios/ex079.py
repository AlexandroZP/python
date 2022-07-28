valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adcionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar!!')
    s_n = str(input('Quer continuar ? [S/N] ')).upper().split()[0]
    if s_n == 'N':
        break
valores.sort()
print(f'Você digitou os valores: {valores}')