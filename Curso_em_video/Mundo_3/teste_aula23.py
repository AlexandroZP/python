# Tratamento de erros e exceções
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# Se der problema. Pode haver mais de um except e é possivel mudar o resultado para cada tipo de exceção
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você informou!!')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: # Se der tudo certo
    print(f'O resultado é {r:.1f}')
finally: # Executado independentemente se der erro ou não
    print('Volte sempre! Muito obrigado!!')