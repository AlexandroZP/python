altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = float(peso / altura**2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("\033[33mAbaixo do peso ideal!")
elif 18.5 <= imc < 25:
    print("\033[32mPeso ideal!")
elif 25 <= imc < 30:
    print("\033[34mSobrepeso!")
elif 30 <= imc < 40:
    print("\033[33mObesidade!")
else:
    print("\033[31mObesidade morbida, cuidado")

