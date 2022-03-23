#Criando a classe Circulo
class Circulo:

    def __init__(self,r):#Será invocada toda as vezes que um objeto da classe for criada.
        self.raio = r;

    def desenha(self):
        pass;
    def imprime(self):
        print("Círculo de raio {}".format(self.raio));

obj_circulo = Circulo(3); #Cria o objeto 'obj_circulo' na classe "Circulo".

#Chama o metdo 'imprime()' da classe circulo.
obj_circulo.imprime();
