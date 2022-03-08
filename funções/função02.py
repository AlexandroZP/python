#Exemplo de função que retorna mais de um valor.
def quociente_resto(x, y):
    quociente = x // y;
    resto = x % y;
    return(quociente, resto);

print("Quociente e resto: ", quociente_resto(9,4));