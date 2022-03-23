def true_false(a,b,limite):
    if a+b > limite:
        return True;
    else:
        return False;
print(true_false(10,10,15));
print(true_false(10,10,20));
print(true_false(10,-5,4));

#Pode também ser feito desta forma

def soma_maior_que_limite(a, b, limite):
    return a + b > limite;
print(soma_maior_que_limite(10,5,15));