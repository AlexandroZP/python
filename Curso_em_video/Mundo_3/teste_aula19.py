# Dicionarios indetificados por {}
from sklearn.exceptions import DataDimensionalityWarning


funcionarios = {'Nome':'Pedro', 'Idade':25}

# Criando dados
funcionarios['Sexo'] = 'M'

# Imprimindo os dados no dicionário
print(funcionarios['Nome'], funcionarios['Idade'], funcionarios['Sexo'])
# Valores
print(funcionarios.values())
# Chaves
print(funcionarios.keys())
# Todos
print(funcionarios.items())


# 'for' com dicionários 'k' = keys 'v' = values 
for k, v in funcionarios.items():
    print(f'{k} é {v}')

# Podemos misturar dicionários com listas
departamento = []
departamento.append(funcionarios.copy()) # 'copy' passa uma cópia do dicionário
print(departamento)
print(departamento[0]['Idade'])

# Adicionando com 'for'
for c in range(0, 3):
    funcionarios['Nome'] = str(input('Nome: '))
    funcionarios['Idade'] = int(input('Idade: '))
    funcionarios['Sexo'] = str(input('Sexo: '))
    funcionarios['Cidade'] = str(input('Cidade: '))
    departamento.append(funcionarios.copy())
    print('Registrando...')


for f in departamento:
    for k, v in f.items():
        print(f'{k:<5}: {v}', end=' ')
    print()

'''print(funcionarios)
# Deletando elementos
del dados['Idade']
print(funcionarios)'''



