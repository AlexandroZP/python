from datetime import date
ano = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

print('Sua idade é {}'.format(idade))
if idade <= 9:
    print('Sua categoria é: \033[32mMirim')
elif idade <= 14:
    print('Sua categoria é: \033[32mInfantial')
elif idade <= 19:
    print('Sua categoria é: \033[32mJunior')
elif idade <= 25:
    print('Sua categoria é: \033[32mSênior')
else:
    print('Sua categoria é: \033[32mMaster')
