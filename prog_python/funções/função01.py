#Exemplo (bem simples) de função em Python.
def f(n,m):
    print("O valor do parâmetro é ", n+m);

f(10,5);

#Exemplo de função que retorna um valor.

def e (n):
    return n;

resultado = e(10);
print("O valor do parâmetro é {}".format(resultado));

#Outro exemplo de função que retorna um valor.
def eleva_ao_quadrado(n):
    return n ** 2;

print("O número {} elevado ao quadrado é {}".format(10,eleva_ao_quadrado(10)));