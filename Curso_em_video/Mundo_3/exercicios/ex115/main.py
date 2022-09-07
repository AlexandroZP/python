from lib.interface import *
from lib.arquivo import *
from time import sleep as slp

arq = 'ex115.txt'

if not arqExiste(arq):
    criarArq(arq)
while True:
    opt = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoa', 'Sair do Sitema'])
    if opt == 1:
        # Opção de listar o conteudo do arquivo
        lerArq(arq)
    elif opt == 2:
        nome = str(input('Nome: ')).strip()
        idade = int_N('Idade: ')
        cadPessoa(arq, nome, idade)
    elif opt == 3:
        break
    slp(2)
