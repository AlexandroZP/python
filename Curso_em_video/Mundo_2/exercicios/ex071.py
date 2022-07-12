valor_inicial = int(input('Digite o valor a ser sacado:'))
valor = valor_inicial
c = 50
t_c = 0
while True:
    if valor >= c:
        valor -= c
        t_c += 1    
    else:
        if t_c > 0:
            print(f'Total de {t_c} cédulas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        t_c = 0
        if valor == 0:
            break

