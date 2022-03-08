def nums(numeros, numero):
    for numero_procurado in numeros:
        if numero_procurado == numero:
            return True;
        else:
            return False;


#Usando o indice
def nums2(numeros, numero):
    for indice in range(len(numeros)):
        if numeros[indice] == numero:
            return True;
    return False;

#Usando Built-in
def nums3(numeros, numero):
    return numero in numeros;

print(nums([10,11,12,13,14], 10));
print(nums2([10,11,12,13,14], 12));
print(nums3([10,11,12,13,14], 9));