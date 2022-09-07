def int_N(msg):
    while True:
        try:
            nI = int(input(f'{msg}'))                
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mNúmero não digitado\033[m')
            return 0
        else:
            return nI

def float_N():
    while True:
        try:
            nF = float(input('Digite um número Real: '))                
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida\033[m')
            return 0
        else:
            break
    return nF