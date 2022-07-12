s = c = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    c += 1
        
print(f'A soma dos {c} valores foi de {s}')