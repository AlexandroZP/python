#Criando dicionario
dicinario_vazio = {}
print("Dicionário vazio: ", dicinario_vazio);


paises = {'BRA': 'Brasil', 'EUA':'Estados Unidos', 'FRA': 'França'};

print("Tipo de um dicionario:", type(paises));

print();

print("Exemplo de dicionário:", paises);

print();
#Modificando um dicionário.
paises['BRA'] = "Brazil";
paises['FRA'] = "France";

#Adicionando elemento.
paises['ESP'] = "Espanha";

print("Dicionário modificado: ", paises);