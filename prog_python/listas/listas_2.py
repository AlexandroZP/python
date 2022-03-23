# Sintaxe da função range ().

inicio = 0;
fim = 100;
passo = 10;

# Convertendo um intervalo em uma lista.
print(list(range(inicio,fim, passo)));

print();
# Ordenando listas. 
lista = [7,25,2,3,30,7,80,100,-1,-15];
print("Lista não ordenada: ", lista);

lista.sort();
print("Lista ordenada: ", lista);

lista.sort(reverse=True);
print("Lista ordenada em ordem decrescente: ", lista);