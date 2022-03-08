A = {0,1,3,5,7,9};
B = {0,2,4,6,8};

# Unindo A com B;
C = A|B; #Pode ser escrever também A.union(B)
print(C);

print();

# Retorna apenas o elemento que está nos dois conjuntos;
C = A & B;#Pode ser escrever também A.intersect(B)
print(C);