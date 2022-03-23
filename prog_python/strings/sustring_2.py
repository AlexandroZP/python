s = "Olá, mundo!";

print(s[::2]); # Imprime os caracteres nos índices pares.
print(s[1::2]) # Imprime os caracteres nos índices ímpares.

frase = "Mundo mundo vasto mundo"
print(frase[::-1]); #inverte a frase;

# Forma mais avançada de formatação de strings
frase_2 = "Um triângulo de base igual a {0} e altura igual a {1} possui área igual {2}.".format(3,4,12);
print(frase_2); 

# Formatação de strongs com f-strings
linguagem = "Python";
frase_3 = f"Progamando em {linguagem}";
print(frase_3);
