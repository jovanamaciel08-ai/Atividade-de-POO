class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = max(0, saldo)
        self.__historico = []  

    def get_numero_conta(self):
        return self.__numero_conta

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito precisa ser positivo.")
            return
        saldo_anterior = self.__saldo
        self.__saldo += valor
        comprovante = f"Depósito: R${valor:.2f} | Saldo anterior: R${saldo_anterior:.2f} | Saldo atual: R${self.__saldo:.2f}"
        self.__historico.append(comprovante)

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque precisa ser positivo.")
            return
        if valor > self.__saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        saldo_anterior = self.__saldo
        self.__saldo -= valor
        comprovante = f"Saque: R${valor:.2f} | Saldo anterior: R${saldo_anterior:.2f} | Saldo atual: R${self.__saldo:.2f}"
        self.__historico.append(comprovante)

    def mostrar_historico(self):
        if not self.__historico:
            print("Nenhuma transação realizada.")
        else:
            print("\n=== Histórico de Transações ===")
            for comprovante in self.__historico:
                print(comprovante)

    def ver_saldo(self):
        print(f"\nSaldo atual: R${self.__saldo:.2f}")