class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
            print(f"Preço atualizado para {preco}.")
        else:
            print("O preço não pode ser negativo.")

    def adicionar_estoque(self, qtd):
        if qtd > 0:
            self.__quantidade += qtd
            print(f"{qtd} unidades adicionadas ao estoque.")
        else:
            print("A quantidade deve ser maior que zero.")

    def remover_estoque(self, qtd):
        if qtd <= 0:
            print("A quantidade deve ser maior que zero.")
        elif qtd > self.__quantidade:
            print("Não há estoque suficiente para remover essa quantidade.")
        else:
            self.__quantidade -= qtd
            print(f"{qtd} unidades removidas do estoque.")

