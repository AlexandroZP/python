alunos = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    alunos.append([nome, [nota_1, nota_2], media])
    s_n = str(input('Deseja continuar ? [S/N] ')).upper().split()[0]
    if s_n == 'N':
        break

print('-=' * 40)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')

print('_' *40)

for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('_' * 45)

while True:
    print()
    m_notas = int(input('Mostrar notas de qual aluno ? (999 interrompe)'))
    if m_notas == 999:
        break
    if m_notas <= len(alunos)-1:
        print(f'Notas de {alunos[m_notas][0]} são {alunos[m_notas][1]}')
    print('_' * 40)
    