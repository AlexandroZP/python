#Exemplo de criação de sets
numeros = [1,2,2,3,3,3];
numeros_distintos = set(numeros);

print("Números: ", numeros);
print("Números distintos: ", numeros_distintos);

print();

#Outra forma
numeros_2 = [1,2,2,3,3,3];
numeros_distintos_2 = set();
for num in numeros_2:
    numeros_distintos_2.add(num);
print("Números: ", numeros_2);
print("Números distintos: ", numeros_distintos_2);