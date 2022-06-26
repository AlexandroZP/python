s = 0
i = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
        i = i + 1
        s = s + n
print('A soma dos {} valores solicitados é {}'.format(i, s))

