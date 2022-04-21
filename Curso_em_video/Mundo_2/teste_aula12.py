nome = str(input('\033[:32mQual é seu nome ?\033[m'))

if nome == 'Gustavo':
    print('\033[:33mQue nome bonito!\033[m')
elif nome == 'Pedro':
    print('\033[:35mSeu nome é bem popular no\033[m \033[:32mB\033[m\033[:33mr\033[m\033[:34ma\033[m\033[:37ms\033[m\033[:34mi\033[m\033[:33ml\033[m\033[:32m!\033[m')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('\033[:36mBelo nome!\033[m')
else:
    print('\033[:31mSeu nome é bem normal.\033[m')
print('\033[:32mTenha um bom dia,{}!\033[m'.format(nome))

