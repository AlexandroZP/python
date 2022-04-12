frase = 'Curso em Video Python'
print(frase[::2]) #começando do 1 indo até o 12(13-1) pulando de 2 em 2
print('Quantas vezes contém a letra "o": ', frase.count('o', 0, 5))
print('Tamanho da  string: ', len(frase))
print('Trocando "Python" por "Android": ', frase.replace('Python', 'Android'))
print('Buscando: ', frase.lower().find('video'))
print('Frase splitada: ', frase.split())
print(frase.casefold())
