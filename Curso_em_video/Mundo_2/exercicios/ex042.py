PL = float(input("Digite o primeiro lado do triangulo: "))
SL = float(input("Digite o segundo lado do triangulo: "))
TL = float(input("Digite o terceiro lado do triangulo: "))

if PL < SL + TL and SL < PL + TL and TL < PL + SL:
    print("\n\033[32mOs lados formam um triangulo\033[34m")
    if PL == SL == TL:
        print("Equilátero!")
    elif PL == SL or SL == TL or TL == PL:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("\n\033[31mOs lados não formam um triangulo!")
