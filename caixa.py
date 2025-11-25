class Caixa:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, preco, quantidade):
        self.produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})

    def get_total(self):
        total = sum(p["preco"] * p["quantidade"] for p in self.produtos)
        return total