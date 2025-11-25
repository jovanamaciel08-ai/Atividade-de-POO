class Animal:
    def __init__(self, nome, especie, idade):
        self.__nome = nome
        self.__especie = especie

        if idade >= 0:
            self.__idade = idade
        else:
            self.__idade = 0
            print("Idade não pode ser negativa. Definida como 0.")

    def get_nome(self):
        return self.__nome  

    def get_especie(self):
        return self.__especie  

    def get_idade(self):
        return self.__idade  

    def envelhecer(self):
        self.__idade += 1
        print(f"{self.__nome} agora tem {self.__idade} anos.")
