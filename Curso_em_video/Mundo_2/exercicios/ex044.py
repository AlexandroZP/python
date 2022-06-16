Preço = float(input("Digite o preço do produto R$"))
metodo = int(input("Selecione o método de pagamento:\n"
      "\n[1] À vista dinheiro/cheque: 10% de desconto"
      "\n[2] À vista cartão: 5% de desconto"
      "\n[3] 2x no cartão"
      "\n[4] 3x ou mais: 20% de juros\n"))
if metodo == 1:
      print("Preço final do produto R${}".format(Preço - Preço * 0.10))
elif metodo == 2:
      print("Preço final do produto R${}".format(Preço - Preço * 0.05))
elif metodo == 3:
      print("Valor das parcelas R${}, preço final R${}".format(Preço/2, Preço))
elif metodo == 4:
      parcelas = int(input("Em quantas parcelas deseja dividir: "))
      print("Valor das parcelas R${}, preço final R${}".format((Preço + Preço * 0.20) / parcelas, Preço + Preço * 0.20))
else:
      print("\033[31m[ERRO]DIGITE UM VALOR VÁLIDO!!!")
