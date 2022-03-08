print("Digite seu nome:");
nome = input();
print("Bem-vindo:", nome);

#Readline()

import sys;
print("Digite dois número:");
idade, peso, altura = map(int, sys.stdin.readline().split());
print("Números:", idade, peso, altura);