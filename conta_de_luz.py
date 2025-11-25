class ContaDeLuz:
    def __init__(self, numero_instalacao, consumo):
        self.__numero_instalacao = numero_instalacao

        if consumo >= 0:
            self.__consumo = consumo
        else:
            self.__consumo = 0
            print("Consumo não pode ser negativo. Definido como 0.")

        self.__valor = self.calcular_valor()

    def get_numero_instalacao(self):
        return self.__numero_instalacao 

    def get_consumo(self):
        return self.__consumo  

    def get_valor(self):
        return self.__valor  

    def set_consumo(self, consumo):
        if consumo >= 0:
            self.__consumo = consumo
            self.__valor = self.calcular_valor()
        else:
            print("O consumo deve ser um número positivo.")
    def calcular_valor(self):
        return self.__consumo * 0.75
