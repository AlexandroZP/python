#Enumerete
print("Usando Enumerate");
for indice, elemento in enumerate(range(-3,3)):
    print(indice,elemento);

#Buscando elemento em uma lista.
print("------------------------------------------------------------------------------");
print("Buscando um elemento em uma lista");
elemento_2 = 10;
estah_presente = False;
lista = [1,2,7,10,15,20,50]; #Lista

for item in lista:
    if item == elemento_2: # Se o item atual for igual ao elemento_2,
        estah_presente = True; #a variavel estah_presente será true.

if estah_presente:
    print("A variável está presente na lista");
else:
    print("A variável não está presente");