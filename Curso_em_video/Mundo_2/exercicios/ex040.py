nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
media = (nota_1 + nota_2) / 2
print('Média: {}'.format(media))
if media < 5.0:
    print('\033[31mO aluno está REPROVADO!')
elif 7 > media >= 5.0:
    print('\033[33mO aluno está de RECUPERAÇÃO!')
else:
    print('\033[32mO aluno está APROVADO!')
