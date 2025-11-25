class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__cpf = cpf  

        self.set_idade(idade)

    def get_nome(self):
        return self.__nome   

    def get_idade(self):
        return self.__idade 

    def get_cpf(self):
        return self.__cpf   

    def set_idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            self.__idade = 0  
            print("Idade não pode ser negativa. Definida como 0.")
