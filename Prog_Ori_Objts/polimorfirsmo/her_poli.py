class Animal:
    def __init__(self):
        pass;

    def locomove(self):
        pass;
class Peixe(Animal):
    
    def locomove(self):
        print("Um peixe nada.");
    
class Elefante(Animal):
    
    def locomove(self):
        print("Um elefante anda.");
    
class Passaro(Animal):

    def locomove(self):
        print("Um passaro voa. ");

peixe = Peixe();
elefante = Elefante();
passaro = Passaro();

peixe.locomove();
elefante.locomove();
passaro.locomove();