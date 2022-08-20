# Manipulando Listas
    #Listas são mutaveis('Podem ser modificadas')
num = [2, 5, 6, 8]
num[2] = 3
print(num)
num.append(7) # Adiciona um elemento no final da lista
print(num)
num.sort(reverse=True) #'.sort'(Ordena a lista) 'reverse=True'(Reverte a lista)
print(num)
print(f'Tamanho da lista {len(num)}')
num.insert(2, 9) #Insere o valor(9) no indice indicado(2) !!Ele não deleta o valor que já está no indice!!
print(num)
num.pop(2) # Deleta o elemento no indice indicado (2)
print(num)
if 4 in num: # Checa se o elemento está na lista
    num.remove(4)
    print(num)
else:
    print('Elemento não está na lista')

for c, v in enumerate(num): # Pega tanto o indice(c) quanto o valor (v) do elemento
    print(f'Elemento {v} no indice {c}')
print('Lista acabou')
'''
for cont in range(0, 5):
    num.append(int(input('Digite o valor a ser adiconado: '))) #Adicionando valor pelo teclado
print(num)
'''
a = [2, 4, 7, 9]
b = a  # Cria uma ligação entre as Listas(A, B) se a B for modificada a A também será.
b[2] = 8
c = a[:] # Cria uma cópia da Lista (A) em uma nova Lista (C). De forma que se a Lista C for alterada, a lista A continuará intacta.
c[2] = 9
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')