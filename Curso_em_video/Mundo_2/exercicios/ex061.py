print('Gerador de PA')
print('-='*20)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 10
while c > 0:
    print(t, ' -> ', end='')
    t += r
    c -= 1
print('FIM')
