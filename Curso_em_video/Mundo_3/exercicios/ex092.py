from datetime import date

ano = date.today().year
funcionarios = {}

funcionarios['Nome'] = str(input('Nome: '))
funcionarios['Idade'] = ano - int(input('Ano de Nascimento: '))
funcionarios['Cttps'] = int(input('Carteira de trabalho (0 para não tem): '))

if funcionarios['Cttps'] != 0:
    funcionarios['Contratação'] = int(input('Ano de contratação: '))
    funcionarios['Salário'] = float(input('Salário: R$'))
    funcionarios['Aposentadoria'] = funcionarios['Idade'] + ((funcionarios['Contratação'] + 35) - ano)

for dado, valor in funcionarios.items():
    print(f'{dado} é: {valor}')
