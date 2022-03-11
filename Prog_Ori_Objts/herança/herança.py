from operator import attrgetter
from xml.dom.minidom import AttributeList


class Veiculo:
    def __init__(self, tipo , chassi, marca, modelo, ano):
        self.tipo = tipo;
        self.chassi = chassi;
        self.marca = marca;
        self.modelo = modelo;
        self.ano = ano;

class Motocicleta(Veiculo): #Indica que a classe 'Motocicleca' é filha da classe 'Veiculo'.
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano); #Invoca o metodo init da classe mãe/superior
        self.cilindrada = cilindrada;

v = Veiculo('carro','9HFHEUIQ86DGQYD634','Ford','Uno','2017');
m = Motocicleta('motocicleta', '5GHGFDYATDF3253GHDGAH','Honda','CG', '2015','90291092');

#Checando se é um instancia
print(isinstance(v,Veiculo), isinstance(v,Motocicleta));
print(isinstance(m,Veiculo), isinstance(m,Motocicleta));
