lista_vazia = [];
print("Lista vazia: ", lista_vazia);
print("Tipo de uma lista: ", type(lista_vazia));

lista_inteiros = [10, 20, 30, 40];
print("Lista de inteiros: ", lista_inteiros);

lista_tipos_diferentes = ["George", "Orwell", 10, 20, 30]
print("Lista de elementos com tipos diferentes: ", lista_tipos_diferentes);

# Aninhamento
lista_aninhada = [1,[2,[3,[4]]],5];
print("Litas aninhada: ", lista_aninhada);

matriz = [[1,2,3], [4,5,6], [7,8,9]];
print("Matriz 3x3: ", matriz);

print("Matriz impressa de outra forma: ")
for lista in matriz:
    for elemento in lista:
        print(elemento, end = '');
    print();