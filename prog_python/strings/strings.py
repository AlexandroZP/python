# Imprimindo uma string
s = "Olá, mundo!";
print(s);

#Tamanho de uma string.
print(len(s));

#Contatenação
print("Meu Brasil " + "brasileiro");


#Substitui uma substring por alguma outra coisa.
s1 = s.replace("mundo","meu abacate"); #Tirou o "mundo" de s e susbtitui por "meu abacate".

print(s1);

# A string s começa com "Olá" ?
print(s.startswith("Olá"));

#Quantas ocorrências da palavra "abacate" a s1 possui ?
print(s1.count("abacate"));