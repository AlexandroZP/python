from time import sleep as slp

def cont(init, n_end, raz):
    print('-=' * 16)

    if raz < 0:
        raz *= -1
    if raz == 0:
        raz = 1

    print(f'Contagem de {init} até {n_end} de {raz} em {raz}')
    if init < n_end:
        for c in range (init, n_end+1, raz):
            print(c, end=' ', flush=True)
            slp(0.5)
    elif init > n_end:
        for c in range(init, n_end-1, -raz):
            print(c, end=' ', flush=True)
            slp(0.5)
    else:
        print(init)
    print('FIM!')


cont(1, 10, 1)
cont(10, 0, 2)

print('-=' * 15)
print('Agora é sua vez de personalizar')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
razao = int(input('Passo: '))
cont(inicio, fim, razao)

    
