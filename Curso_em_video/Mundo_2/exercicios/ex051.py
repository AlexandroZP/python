print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
pt = int(input('Primeiro termo: ')) #Primeiro termo
r = int(input('Razão: ')) #Razão
for c in range(0, 10):
    print('{}'.format(pt), end=' -> ')
    pt = pt + r
print('ACABOU!')
