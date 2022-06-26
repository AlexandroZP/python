from time import sleep
n = int(input('Entre com o número inicial: '))

for c in range(n, 0, -1):
    print(c)
    sleep(1)
print('\033[32mExplodiu os fogos de artifícios!')