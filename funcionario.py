class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo

        if salario >= 0:
            self.__salario = salario
        else:
            self.__salario = 0
            print("Salário negativo não é permitido. Definido como 0.")

    def get_nome(self):
        return self.__nome   

    def get_cargo(self):
        return self.__cargo  

    def get_salario(self):
        return self.__salario  

    def aumentar_salario(self, percentual):
        if percentual > 0:
            aumento = self.__salario * (percentual / 100)
            self.__salario += aumento
            print(f"Salário aumentado em {percentual}%. Novo salário: {self.__salario}")
        else:
            print("O percentual deve ser maior que zero.")
