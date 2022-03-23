arquivo = open('inputs-outputs/input-arquivos/arquivo.txt', 'r');
conteudo = arquivo.read();
print(conteudo);

print("=================================================================");
# Se o arquivo for grande
arquivo_2 = open('inputs-outputs/input-arquivos/arquivo.txt', 'r');
for linha in arquivo_2.readlines():
    print(linha);

