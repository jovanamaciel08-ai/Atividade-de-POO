class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = max(0, idade)
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("Idade não pode ser negativa.")

    def get_cpf(self):
        return self.__cpf