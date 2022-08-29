def leiaDinheiro(msg):
    valido = False
    while not valido:

        dinheiro = str(input(msg)).replace(',', '.').strip()

        if dinheiro.isalpha() or dinheiro == "":

            print(f'\033[31m ERRO: \"{dinheiro}"\ é um preço invalido\033[m')

        else:

            valido = True
            return float(dinheiro)

def leiaInt(msg):
    n = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            n = int(num)
            return n
        else:
            print('\033[0;31mERRO!! Digite um valor válido.\033[m')
