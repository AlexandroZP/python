def duplicados(numeros):
    return len(numeros) - len(set(numeros));
print(duplicados([1,1,2,2,2,3,3,4,4]));