n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/ 2
if m >= 5:
    print('Sua média foi {}, parabéns você foi aprovado!'.format(m))
else:
    print('Sua média foi {}, você é uma decepção!'.format(m))
print('____________')