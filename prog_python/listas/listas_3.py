lista = [4,7,2,5,-1,7];
print("Lista original antes da ordenação: ",lista);

lista_ordenada = sorted(lista);
print("Lista ordenada: ", lista_ordenada);

print("A lista original permanece inalterada: ", lista);

print();
#Cria uma lista vazia
lista_2 = [];

#Adiciona elementos à lista
lista_2.append("P");
lista_2.append("Y");
lista_2.append("T");
lista_2.append("H");
lista_2.append("O");
lista_2.append("N");

print(lista_2);

#Modificando a lista
lista_2[1] = 'A';
lista_2[3] = 'R';
lista_2[4] = 'i';
lista_2[5] = 'A';

print(lista_2);