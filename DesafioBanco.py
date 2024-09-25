# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from datetime import date

# Classe Historico para armazenar transações
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Interface Transacao e suas implementações para Saque e Deposito
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.historico.adicionar_transacao(self)
            print(f"Depósito de R$ {self.valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if len(conta.saques_diarios) >= 3:
            print("Você atingiu o limite de 3 saques diários.")
        elif self.valor > 500:
            print("O valor do saque excede o limite de R$ 500,00 por saque.")
        elif self.valor > conta.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            conta.saldo -= self.valor
            conta.saques_diarios.append(self.valor)
            conta.historico.adicionar_transacao(self)
            print(f"Saque de R$ {self.valor:.2f} realizado com sucesso!")

# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

# Classe PessoaFisica, que herda de Cliente
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Classe Conta
class Conta:
    def __init__(self, cliente, numero, agencia):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
        self.saques_diarios = []

    def saldo(self):
        return self.saldo

    def sacar(self, valor):
        saque = Saque(valor)
        self.cliente.realizar_transacao(self, saque)

    def depositar(self, valor):
        deposito = Deposito(valor)
        self.cliente.realizar_transacao(self, deposito)

# Classe ContaCorrente, que herda de Conta
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite, limite_saques):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques

# Função principal
def main():
    cliente = PessoaFisica(cpf="12345678900", nome="Marcos Rogato", data_nascimento=date(1990, 5, 15), endereco="Rua Exemplo, 123")
    conta_corrente = ContaCorrente(cliente, numero=1234, agencia="0001", limite=1000.0, limite_saques=3)

    cliente.adicionar_conta(conta_corrente)

    while True:
        print("\n--- MENU ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver saldo")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: R$ "))
            conta_corrente.depositar(valor)

        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: R$ "))
            conta_corrente.sacar(valor)

        elif opcao == '3':
            print(f"Saldo atual: R$ {conta_corrente.saldo:.2f}")

        elif opcao == '4':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
