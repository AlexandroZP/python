from time import  sleep
pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
option = 0
while option != 5:
    print('[ 1 ] Somar\n'
          '[ 2 ] Multiplicar\n'
          '[ 3 ] Maior\n'
          '[ 4 ] Novos números\n'
          '[ 5 ] Sair do programa')
    option = int(input('>>>Qual é a sua opção ? '))
    if option == 1:
        print('A soma entre {} e {} é: {}'.format(pv, sv, pv + sv))
    elif option == 2:
        print('A multiplicação entre {} e {} é: {}'.format(pv, sv, pv * sv))
    elif option == 3:
        if sv > pv:
            print('O segundo número é o maior = {}'.format(sv))
        elif pv > sv:
            print('O primeiro número é o maior = {}'.format(pv))
        else:
            print('Os números são iguais!')
    elif option == 4:
        print('Digite os novos valores abaixo.')
        pv = int(input('Primeiro valor: '))
        sv = int(input('Segundo valor: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!!')
    sleep(2)
    print('=-'*20)
print('Programa finalizado!!')