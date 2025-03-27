class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo: {self.saldo} do titular {self.titular} na conta {self.numero}")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Valor depositado{valor}")
    
    def sacar(self, valor):
        self.saldo -= valor
        print(f"Valor retirado {valor}")