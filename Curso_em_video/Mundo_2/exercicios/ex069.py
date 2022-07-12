qtF = qtM = qt_idade = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        qt_idade += 1
    
    if sexo == 'F' and idade < 20:
        qtF += 1
    elif sexo == 'M':
        qtM += 1
    
    s_n = ' '
    while s_n not in 'SN':
        s_n = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    
    if s_n == 'N':
        break
print(f'\nHomens cadastrados = {qtM}\n',
    f'\nMulheres menores de 20 anos = {qtF}\n',
    f'\nMaiores de idade = {qt_idade}')
