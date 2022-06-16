fn = int(input('Primeiro número: '))
sn = int(input('Segundo número: '))
print('\033[32m=\033[m'*60)
if fn == sn:
    print('\033[31mOs números são iguais!\033[m')
elif fn > sn:
    print('\033[34mO \033[33mPRIMEIRO\033[m \033[34mvalor é o  maior!\033[m')
else:
    print('\033[34mO \033[33mSEGUNDO\033[m \033[34mvalor é o maior!')
