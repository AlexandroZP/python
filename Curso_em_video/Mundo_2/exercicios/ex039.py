from datetime import date
gênero = str(input('Seu gênero: ')).strip().lower()
n_ano = int(input('O ano de nasciemnto: '))
a_atual = date.today().year
idade = a_atual - n_ano
print('\033[34m#\033[m'*50)
print('Quem nasceu em {} nascimento tem {} anos em {}.\n'.format(n_ano, idade, a_atual))
if gênero == 'homem':
    if idade == 18:
        print('\033[33mSeu alistamento é este ano!\033[m\n')
    elif idade < 18:
        res = 18 - idade
        print('\033[32mFaltam {} ano(s) para o seu alistamento!\033[m'.format(res))
        print('Seu alistamento será em {}\n'.format(a_atual+res))
    else:
        res = idade - 18
        print('\033[31mVocê já deveria ter se alistado há {} ano(s) atrás!\033[m'.format(res))
        print('Seu alistamento foi en {}\n'.format(a_atual-res))
print('Obrigado por testar o programa!')

