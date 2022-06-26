hmi = 0
nhmi = ''
mmi = 0
somaI = 0
mediaI = 0
for p in range(1, 5):
    print('----- {}° Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower().strip()
    somaI += idade
    if sexo == 'm' and idade > hmi:
        hmi = idade
        nhmi = nome
    if sexo == 'f' and idade < 20:
        mmi += 1

mediaI = somaI / 4
print('A média de idade do grupo é de {} anos'.format(mediaI))
print('O homem mais velho tem {} anos é {}'.format(hmi, nhmi))
print('Há {} mulheres menores do que 20 anos'.format(mmi))

