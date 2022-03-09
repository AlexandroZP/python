paises = {'BRA': 'Brasil', 'EUA':'Estados Unidos', 'FRA': 'França'};

print("EUA:", paises['EUA']);

print();

#Pecorrendo um dicionario
for sigla, nome in paises.items():
    print(sigla + " = " + str(nome));