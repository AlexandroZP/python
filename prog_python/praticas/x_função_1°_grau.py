def passa_lado(n1,n2):
    n1 = -n1;
    if n1 < 0:
        n1 = n1*-1;
        n2 = n2*-1;
    x = n2 / n1;
    return x;
    
print("Digite o primeiro número: ");
n1 = int(input());
print("Digite o segundo número: ");
n2 = int(input());
x = 0;
print("Função: {0} = {1}x {2}".format(x,n1,n2));
print(passa_lado(n1,n2));
