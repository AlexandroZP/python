t = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 10
ct = 10
while c > 0:
    print(t, '-> ', end='')
    t += r
    c -= 1
    if c == 0:
        print('PAUSA')
        ut = t
        c = int(input('Quantos termos você quer amostrar agora ? '))
        ct += c
        t = ut
print('A progressão foi finalizada com {} termos mostrados'.format(ct))
