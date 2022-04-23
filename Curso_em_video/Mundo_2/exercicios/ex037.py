n = int(input('Digite o número a ser convertido: '))
print('\033[32m=\033[m'*40)
option = int(input('Como deseja converter ?\n\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n: '))
print('\033[32m=\033[m'*40)
if option == 1:
    print('{} convertido em \033[34mBINÁRIO\033[m é igual à {}'.format(n, bin(n)[2:]))
elif option == 2:
    print('{} convertido em \033[34mOCTAL\033[m é igual à {}'.format(n, oct(n)[2:]))
elif option == 3:
    print('{} convertido em \033[34HEXADECIMAL\033[m é igual {}'.format(n, hex(n)[2:]))
else:
    print('ERRO! Digite um valor válido')
