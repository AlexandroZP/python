
valores = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    s_n = str(input('Quer continuar ? [S/N] ')).upper().split()[0]
    if s_n == 'N':
        break
valores.sort(reverse=True)

print('-=' * 40)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em  ordem decrescente são {valores}.')

if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')