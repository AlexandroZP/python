valores= []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > valores[-1]:
        valores.append(valor)
        print(f'Valor {valor} adicionado ao final da lista')
    else:
        indice = 0
        while indice < len(valores):
            if valor <= valores[indice]:
                valores.insert(indice, valor)
                print(f'Valor adicionado na posição {indice}')
                break
            indice += 1
print('-=' * 30)
print(f'Os valores digitados foram {valores}')
