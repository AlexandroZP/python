m_valores = [[], [], []]

for l in range (0, 3):
    for c in range (0,3):
        valor = int(input(f'Digite um valor para [{l}][{c}]: '))
        m_valores[l].append(valor)

#print(m_valores)
for c in range(0, len(m_valores)):
    for valor in m_valores[c]:
        print(f'[ {valor:^5} ]', end=' ')
    print() 