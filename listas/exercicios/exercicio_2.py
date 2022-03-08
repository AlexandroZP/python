def conta_elementos(numeros):
    elementos_unicos = set(numeros);
    return len(elementos_unicos);


print(conta_elementos([10,10,3,3,4,5,5,6]));