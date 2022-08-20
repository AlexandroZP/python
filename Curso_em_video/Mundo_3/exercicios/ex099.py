from time import sleep as slp

def maior_v(* num):
    print('-=' * 40)
    print('Analisando os valores passados...')
    slp(0.75)
    maior = 0
    if len(num) > 0:
        for n in num:
            if  n > maior:
                maior = n
            print(n, end=' ', flush=True)
            slp(0.75)
    print(f'Foram informados {len(num)} valores.')
    print(f'O maior valor informado foi {maior}')


maior_v(2,9,4,5,7,1)
maior_v(4, 7, 0)
maior_v(1, 2)
maior_v(6)
maior_v()