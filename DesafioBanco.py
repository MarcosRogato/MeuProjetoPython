# -*- coding: utf-8 -*-
class Banco:
    def __init__(self):
        self.saldo = 0.00
        self.saques_diarios = []
        self.depositos = []

    def depositar(self, valor):
        if valor > 0:
            self.depositos.append(valor)
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if len(self.saques_diarios) >= 3:
            print("Você atingiu o limite de 3 saques diários.")
        elif valor > 500:
            print("O valor do saque excede o limite de R$ 500,00 por saque.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saques_diarios.append(valor)
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def extrato(self):
        if not self.depositos and not self.saques_diarios:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for i, dep in enumerate(self.depositos, 1):
                print(f"Depósito {i}: R$ {dep:.2f}")
            for i, saq in enumerate(self.saques_diarios, 1):
                print(f"Saque {i}: R$ {saq:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")

# Função para exibir o menu e capturar a escolha do usuário
def menu():
    print("\n--- MENU ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

def main():
    conta = Banco()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: R$ "))
            conta.depositar(valor)

        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: R$ "))
            conta.sacar(valor)

        elif opcao == '3':
            conta.extrato()

        elif opcao == '4':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
