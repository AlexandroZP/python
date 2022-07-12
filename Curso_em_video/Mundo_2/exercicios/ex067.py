while True:
    n = int(input('Quer ver a tabuada de qual valor ?'))
    if n < 0:
        break
    print('-'*20)
    for sn in range(0,11):
        print(f'{n} x {sn} = {n*sn}')
    print('-'*20)