

def voto(ano):
    from datetime import date


    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 16:
        return f'Com {idade} Voto Negado!'
    elif 18 <= idade < 65:
        return f'Com {idade} Voto obrigatorio'
    else:
        return f'Com {idade} Voto opcional'
    


ano = int(input('Digite o ano de seu nascimento: '))

print(voto(ano))