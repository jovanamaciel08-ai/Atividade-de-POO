class Caixa:
    def __init__(self):
        self.__produtos = []  
        self.__total = 0      

    
    def get_total(self):
        return self.__total   

    def adicionar_produto(self, nome, preco):
        if preco >= 0:
            self.__produtos.append((nome, preco))  
            self.__total += preco                 
            print(f"Produto {nome}.\nPreço: {preco}.\nTotal agora: {self.__total}")
        else:
            print("O preço do produto deve ser positivo.")
