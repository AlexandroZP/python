bolo = ['farinha', 'trigo', 'ovo', 'leite', 'manteiga'];
bolo.append(['açucar', 'fermento']);
print(bolo);

#Usando 'EXTEND'
bolo_2 = ['farinha', 'trigo', 'ovo', 'leite', 'manteiga'];
bolo_2.extend(['açucar', 'fermento']);
print(bolo_2);

print();
#Inserindo elementos em posições especificas
lista = ['P','T','H','N'];
lista.insert(1,"Y");
lista.insert(4,"O");
print(lista);

print();
#Removendo elementos
lista_2 = ['A', 'F', 'S', 'Z', 'O'];
print("Lista original: ", lista_2);

lista_2.remove("S");
print("Removendo um elemento: ", lista_2);

#Em posição especifica usamos 'del'
lista_3 = ['A', 'F', 'S', 'Z', 'O'];
del lista_3[2];
print("Removendo um elemento especifico: ", lista_3);