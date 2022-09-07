from lib.interface import cabeçalho, linhas
from lib.maths import int_N


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um error na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '') 
            print(f'{dado[0]:<30}{dado[1]:3>} anos')
        print(linhas())
    finally:
        a.close()


def cadPessoa(arq, nome='None', idade=0):
    try:
        a = open(arq, 'at')
    except :
        print('ERRO: ao ler arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO: Ao tentar registrar!!')
        else:
            print(f'Novo registro de {nome}')
        finally:
            a.close()
    