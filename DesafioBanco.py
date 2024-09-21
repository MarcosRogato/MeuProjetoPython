# -*- coding: utf-8 -*-
class Cliente:
    def __init__(self, nome, rg, cpf):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf

class Conta:
    def __init__(self, cliente):
        self.cliente = cliente
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
            print(f"Extrato da conta de {self.cliente.nome}:")
            for i, dep in enumerate(self.depositos, 1):
                print(f"Depósito {i}: R$ {dep:.2f}")
            for i, saq in enumerate(self.saques_diarios, 1):
                print(f"Saque {i}: R$ {saq:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")


class Banco:
    def __init__(self):
        self.clientes = {}
        self.contas = {}

    def cadastrar_cliente(self, nome, rg, cpf):
        if cpf in self.clientes:
            print("CPF já cadastrado.")
        else:
            cliente = Cliente(nome, rg, cpf)
            self.clientes[cpf] = cliente
            self.contas[cpf] = Conta(cliente)
            print(f"Cliente {nome} cadastrado com sucesso!")

    def acessar_conta(self, cpf):
        if cpf in self.contas:
            return self.contas[cpf]
        else:
            print("Conta não encontrada.")
            return None


# Função para exibir o menu principal
def menu_principal():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Cadastrar cliente")
    print("2. Acessar conta")
    print("3. Sair")


# Função para exibir o menu de operações da conta
def menu_conta():
    print("\n--- MENU CONTA ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Voltar ao menu principal")


# Função principal
def main():
    banco = Banco()
    
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            rg = input("Digite o RG do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            banco.cadastrar_cliente(nome, rg, cpf)

        elif opcao == '2':
            cpf = input("Digite o CPF para acessar a conta: ")
            conta = banco.acessar_conta(cpf)

            if conta:
                while True:
                    menu_conta()
                    opcao_conta = input("Escolha uma opção: ")

                    if opcao_conta == '1':
                        valor = float(input("Digite o valor a ser depositado: R$ "))
                        conta.depositar(valor)

                    elif opcao_conta == '2':
                        valor = float(input("Digite o valor a ser sacado: R$ "))
                        conta.sacar(valor)

                    elif opcao_conta == '3':
                        conta.extrato()

                    elif opcao_conta == '4':
                        break

                    else:
                        print("Opção inválida! Tente novamente.")

        elif opcao == '3':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
