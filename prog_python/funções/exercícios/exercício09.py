def maior_que(numeros,limite):
    i = 0;
    while i < len(numeros):
        if numeros[i] > limite:
            return i;
        i+=1
    return -1;
print(maior_que([5,7,8,10],9));
print(maior_que([5,7,8,10],19));
