def imprimir(a,b,limite):
    if a > limite and b > limite:
        return 2;
    elif a > limite or b > limite:
        return 1;
    else:
        return 0;
print(imprimir(3,3,2));
print(imprimir(2,3,2));
print(imprimir(2,2,2));
    