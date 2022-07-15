from itertools import count


times = ('Palmeiras', 'Corinthians', 'Internacional', 'Atlético-MG', 'Fluminense',
'Athletico-PR', 'São Paulo', 'Santos', 'Flamengo', 'Botafogo', 'Bragantino', 'Goiàs',
'Cuibá', 'Coritiba', 'América-MG', 'Avaí', 'Ceará SC', 'Atlético-GO', 'Juventude', 'Fortaleza')

print(f'Os cinco primeiros colocados são: \n{times[:5]}')
print(f'\nOs quatro ultimos colocados são: \n{times[-4:]}')
print(f'\nTime em ordem alphabetica: \n{sorted(times)}')
print(f'\n Cuibá é o {times.index("Cuibá")+1}° colocado')