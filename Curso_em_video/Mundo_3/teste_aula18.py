# Listas compostas

teste = []

teste.append('Alexandro')
teste.append(22)
print(teste)

galera = []
galera.append(teste[:]) # Jogando uma copia de uma lista dentro da outra
print(galera)

teste[0] = 'Regina'
teste[1] = 40
galera.append(teste[:])
print(galera)

galera_2 = [['João', 24], ['Maria', 27], ['Ana', 34], ['Marta', 45]] #criando lista com listas
print(galera_2[2][1])

for pessoa in galera_2:
    print(f'{pessoa[0]} tem {pessoa[1]} de idade') # Imprimindo todos os nomes da lista


pessoas = []
dado = []

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
print(pessoas)

for pessoa in pessoas:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
    else:
        print(f'{pessoa[0]} é menor de idade')
    