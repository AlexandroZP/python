def leiaInt(msg):
    n = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            n = int(num)
            return n
        else:
            print('\033[0;31mERRO!! Digite um valor válido.\033[m')


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'O valor digitado foi {n}')