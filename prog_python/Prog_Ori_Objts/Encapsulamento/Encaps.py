class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome;
        self.cargo = cargo;
        self.valor_hora_trabalhada = valor_hora_trabalhada;
        self.__horas_trabalhadas = 0;
        self.__salario = 0;


    @property
    def salario(self):
        return self.salario;

    @salario.setter
    def salario(self,novo_salario):
        raise ValueError("Impossivel alterar salario diretamente. Use a funcão calc_salario().");


    def regis_hora_trabalhada(self):
        self.horas_trabalhadas += 1;
        
    def calc_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada;


pedro = Funcionario('Pedro', 'Gerente de vendas', 50);
print(pedro);
