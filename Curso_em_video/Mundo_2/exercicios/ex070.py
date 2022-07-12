p_mBarato = qt_mMil = p_total = c = 0
n_pmBarato =  ''


while True:
    print('-' * 30)
    n_produto = str(input('Nome do produto: '))
    p_produto = float(input('Preço: R$'))
    c+=1
    p_total += p_produto

    if p_produto > 1000.00:
        qt_mMil += 1

    if c == 1 or  p_produto < p_mBarato:
        n_pmBarato = n_produto
        p_mBarato = p_produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total da compra foi {p_total:.2f}',
    f'\nTemos {qt_mMil} produtos custando mais de R$1000.00',
    f'\nO produto mais barato foi {n_pmBarato} que custa R${p_mBarato:.2f}')