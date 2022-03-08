#Criando lista dentro de um laço for
frutas = ['maçã', 'banana', 'amora', 'manga'];
plurais_frutas = [];

for fruta in frutas: 
    plural = fruta + 's'; #Adicona o 'S' no final de cada elemento da lista
    plurais_frutas += [plural]; #Passa o elemento com o 'S' para dentro da outra lista
print(plurais_frutas);