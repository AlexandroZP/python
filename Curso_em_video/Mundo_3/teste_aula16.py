# Variaveis compostas
'''
Tuplas
° Se utiliza () para declaração (Não é obrigatorio).
° São imutaveis(Depois de definida não pode ser mudada)
Listas
Dicionários
'''
# Ex tupla
n = 2,3,1,4
'''

print(n) # Imprime a tupla/lista inteira
print(n[0]) # Imprime o valor que está no indice indicado entre []
print(n[-1])# Imprime o ultimo valor
print(len(n)) # Imprime a quantidade de elementos dentro da tupla/lista
print(n[1:]) # Imprime a partir do elemento [1]
print(n[:3]) # Imprime todos os valores antes de [3]
print('-=' * 30)

'''

# Imprimindo todos os elementos
'''
for c in n:
    print(f'Contando... {c}')
print('-' * 20)

for cont in range(0, len(n)):
    print(f'Contando... {n[cont]}')

for indice, cont in enumerate(n): # A função enumerate() retorna tanto o indice e o "nome" do elemento
    print(f'O número {cont} está no indice {indice}')
'''
# Ordenando tupla
#print(sorted(n))

# Juntando tuplas
i = 7,4,8,6

y = n + i

print(y)
print(y.count(4)) # A função count() nos diz quantas vezes o elemento indicado aparece na tupla
print(y.index(4, 4)) # A função index() nos diz qual o primeiro indice está o elemnto indicado a partir do indice indicado

# Tuplas aceitam mais de um tipo de variavel
k = ('Alex', 3, 4,5, True)
print(k)