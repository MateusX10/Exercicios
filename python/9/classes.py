class Cliente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novoCPF):
        if len(novoCPF) != 11:
            print("\033[1;31mO seu CPF é inválido. Por favor, digite o novo CPF abaixo: ")

            while True:
                novoCPF = str(input("Novo CPF: "))

                if len(novoCPF) == 11:
                    break

                print("\033[1;31mCPF inválido. Por favor, tente novamente.\033[m")

        self._cpf = novoCPF

class ContaBancaria:

    def __init__(self, numero, cliente, saldo=0):

        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo


    def depositar(self, valor):

        self.saldo += valor

        print(f"\033[1;32mSaldo atualizado para R${valor:.2f}")


    def sacar(self, valor_do_saque):

        if valor_do_saque > self.saldo:

            print("\033[1;31mVocê não tem o suficiente.\033[m")
            return


        self.saldo -= valor_do_saque



