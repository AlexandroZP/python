def aumentar(aumento=0, valor=0, form=False):
    res = valor + (valor * (aumento / 100))
    return res if form is False else moeda(res)


def diminuir(redução=0, valor=0, form=False):
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


