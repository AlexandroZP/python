# Funções
def soma(a, b):
    s = a + b
    print(s)


# Empacotar parâmetro
def contador( * num): # "num" se tornará uma Tupla
    print('Recebi os valores: ', end='')
    for valor in num:
        print(valor, end=' ')
    print(f'\nSão ao todo {len(num)} números.')


# Dobra os valores na lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa principal
soma(4, 7)
soma(b = 7, a = 8) # Específicando !! Se especificar um  parâmetro será necessario específicar o outro
soma(2, 5) 

contador(5, 7, 8 , 9)

valores = [5, 6, 4, 3]
dobra(valores)
print(valores)
