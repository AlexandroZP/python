expressão = str(input('Digite a expressão: '))
cont = []
for simb in expressão:
    if simb == '(':
        cont.append('(')
    elif simb == ')':
        if len(cont) > 0:
            cont.pop()
        else:
            cont.append(')')
if len(cont) == 0:
    print('Sua expressão é valida!!')
else:
    print('Sua expressão está errada!!')