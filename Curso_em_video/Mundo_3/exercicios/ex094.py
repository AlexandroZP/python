funcionarios = []


# Leitura dos dados
while True:
    funcionario = {}
    funcionario['Nome'] = str(input('Nome: '))

    # Checa se o Sexo foi digitado corretamente
    while True:
        funcionario['Sexo'] = str(input('Sexo: [M/F/NB/GF]')).upper()
        if funcionario['Sexo'] in 'MF':
            break
        elif funcionario['Sexo'] == 'NB':
            break
        elif funcionario['Sexo'] == 'GF':
            break
        else:
            print('ERRO! Por favor, digite apenas valores válidos!!')
    funcionario['Idade'] = int(input('Idade: '))

    funcionarios.append(funcionario.copy())

    # Checa se a pessoa digitou o 'continuar ou não' corretamente
    while True:
        s_n = str(input('Quer Continuar ? [S/N]')).upper().split()[0]
        if s_n in 'SN':
            break
        print('ERRO! Responda apenas S ou N !!')   
    if s_n == 'N':
        break

print('-=' * 40)
print(f'A) Ao todo temos {len(funcionarios)} pessoas cadastradas.')


# Análise de dados

# Calcula a média de idade
totalIdade = mediaIdade = 0

for funcionario in funcionarios:
    totalIdade += funcionario['Idade']
mediaIdade = totalIdade / len(funcionarios)
print(f'B) A média de idade é de {mediaIdade:5.2f}.')


# Cálcula o total de mulheres cadastradas
print('C) As mulheres cadastradas foram ', end='')
for funcionario in funcionarios:
    if funcionario['Sexo'] == 'F':
        print(funcionario['Nome'], end=' ')


# Lista as pessoas acima da média de idade
print('\nD) Lista de pessoas acima da média de idade: ')
for funcionario in funcionarios:
    if funcionario['Idade'] > mediaIdade:
        print(f'    Nome: {funcionario["Nome"]}; Sexo: {funcionario["Sexo"]}; Idade: {funcionario["Idade"]}')
