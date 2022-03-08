def imprimir(n):
    for num in range(n):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz");
        elif num % 3 == 0:
            print("Buzz");
        elif num % 5 == 0:
            print("Fizz");
        else:
            print(num);
imprimir(10);