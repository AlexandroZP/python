'''print(input.__doc__);
help(input)'''

# Funções dois

# DocStrings


def contador(i,f,p):
    """->Faz uma contagem e mostra em tela...
       Args:
        i:Inicio da contagem
        f:Fim da contagem
        p:Passo(Razão)
        return: sem retorno
    """
    for c in range(i,f+1,p):
        print(c, end=' ')
    print('Fim!!')


# help(contador)


# Paramêtros opcionais
def soma(a=0, b=0, c=0):
    """-> Soma os números passados pelos paramêtros...

    Args:
        a (int, optional): Defaults to 0.
        b (int, optional): Defaults to 0.
        c (int, optional): Defaults to 0.
    """
    soma= a + b + c
    print (soma);



#soma(2,2)
#soma(2,2,3)
#help(soma)

# Variaves locais
def teste(b):
    a = 8 # Nova variável A é declarada de modo que variável A de fora não se altere.
    b += 4
    c = 2
    print(f'A dentro de "teste()" vale {a}')
    print(f'B dentro de "teste()" vale {b}')
    print(f'C dentro de "teste()" vale {c}')


#a = 5
#teste(a)
#print(f'A fora de "teste()" vale {a}')

def teste2(b):

    global a # A variável A dentro da função se torna o valor global de A.
    a = 8 
    b += 4
    c = 2
    print(f'A dentro de "teste()" vale {a}')
    print(f'B dentro de "teste()" vale {b}')
    print(f'C dentro de "teste()" vale {c}')


#a = 5
#teste2(a)
#print(f'A fora de "teste()" vale {a}')

# Função com retorno
def somar(a=0, b=0, c=0):
    s = a+b+c
    return s


r1 = somar(2,3,5)
r2 = somar(3,3)
r3 = somar(1)
print(f'{r1} {r2} {r3}')

