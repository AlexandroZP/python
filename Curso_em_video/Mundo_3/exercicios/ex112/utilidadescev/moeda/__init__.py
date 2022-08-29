def aumentar(aumento=0, valor=0, form=False):
    res = valor + (valor * (aumento / 100))
    return res if form is False else moeda(res)


def reduzir(redução=0, valor=0, form=False):
    res = valor - (valor * (redução / 100))
    return res if form  is False else moeda(res)


def dobro(valor=0, form=False):
    res= valor * 2
    return res if form  is False else moeda(res)


def metade(valor=0, form=False):
    res = valor / 2
    return res if form  is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço, aumento=10, redução=10, form=False):
    print('-' * 35)
    print('\tRESUMO DO VALOR')
    print('-' * 35)

    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço : \t{dobro(preço, form)}')
    print(f'Metade do preço: \t{metade(preço, form)}')
    print(f'{aumento}% de aumento: \t{aumentar(aumento, preço, form)}')
    print(f'{redução}% de redução: \t{reduzir(redução, preço, form)}')
    print('-' * 35)