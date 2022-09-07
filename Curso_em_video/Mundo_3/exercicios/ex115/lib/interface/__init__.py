from lib.maths import int_N


def linhas(tam=42):
    return '-' * tam


def cabeçalho(msg):
    print(msg.center(42))
    print(linhas())


def menu(list):
    cabeçalho('\033[35mMENU PRINCIPAL\033[m')

    for index, item in enumerate(list):
        print(f'\033[33m{index+1} - {item}\033[m')

    print(linhas())
    
    opção = int_N('\033[32mSua Opção: \033[m')
    print(linhas())
    return validacao(opção, list)
                  

def validacao(opt, opções):    
    try:
        print(linhas())
        print(f'\033[34m{opções[opt-1]}\033[m'.center(42))
        print(linhas())
        if opt == 3:
            cabeçalho('SAINDO DO SISTEMA!!')
    except IndexError:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    else:
        return opt



