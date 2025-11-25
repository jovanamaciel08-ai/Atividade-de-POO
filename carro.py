class Carro:
    def __init__(self, modelo, ano):
        self.__modelo = modelo
        self.__ano = ano
        self.__velocidade = 0

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    def get_velocidade(self):
        return self.__velocidade

    def acelerar(self, valor):
        if valor > 0:
            self.__velocidade = min(200, self.__velocidade + valor)

    def frear(self, valor):
        if valor > 0:
            self.__velocidade = max(0, self.__velocidade - valor)