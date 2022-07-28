print('Digite quatro valores: ')
numeros = (int(input('1° ')), int(input('2° ')), int((input('3° '))), int((input('4° '))))
print('-=' * 40)
print(f'O número 9 aparece {numeros.count(9)} vez(es)')

if 3 in numeros:
    print(f'O número 3 se encontra na {numeros.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado')
print('-=' * 40)

print('Numeros pares são: ', end='')
for p in numeros:
    if p % 2 == 0:
        print(p , end=' ')