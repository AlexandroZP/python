
def fatorial(num=0, show=False):
    """->Calcula o fatorial desta função

    Args:
        num (int): Valor a ser calculado
        show (bool, optional):Se irar amostra apenas o resultado(False) ou o calculo inteiro(True). Defaults to False.

    Returns:
        String:Resultado do fatorial
    """

    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c}', end=' ')
            if c == 1:
                break;
            print('x', end=' ')
    return f'= {f}'


help(fatorial)
print(fatorial(5, True))
