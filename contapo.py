
#from contapo import Conta

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo: {self.__saldo} do titular {self.__titular} na conta {self.__numero}")

    def depositar(self, valor):
        self.__saldo += valor
        #print(f"Valor depositado{valor}")
    
    def sacar(self, valor):
        self.__saldo -= valor
        #print(f"Valor retirado {valor}")
    
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite