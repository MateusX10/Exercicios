class ContaBancaria:

    def __init__(self, titular: str, saldo:float,limite: float):

        self.titular = titular
        self.limite = 20000
        self.saldo = saldo


    # obtém o valor do saldo da conta
    @property
    def saldo(self)->None:

        return self._saldo

    # define o valor do saldo da conta
    @saldo.setter
    def saldo(self, valor)->None:

        # verifica se o valor da conta excede o limite, que no caso é R$20000.
        if valor > 20000:

            print("\033[1;31mValor a ser depositado excede o limite da conta.Por favor, altere o valor a ser depositado.\033[m")


            # caso exceda, é requisitado que seja depositado um novo valor
            while True:

                valor = float(input("\033[1;33mNovo valor a ser depositado: R$\033[m"))

                if valor < self.limite:

                    break

                print("\033[1;31mValor excede limite da conta.Por favor, tente um valor menor.\033[m")

        self._saldo = valor


    def depositar(self, valor_a_ser_depositado:float)->None:
        '''-> Deposita um valor na conta

            Parâmetros:

                valor_a_ser_depositado(float): valor a ser depositado na conta
                return: sem retorno
        '''
        
        # verificaq se o valor a ser depositado excede o limite ou se o valor a ser depositado somado com o saldo da conta excede o limite 
        if valor_a_ser_depositado > self.limite or valor_a_ser_depositado + self.saldo > self.limite:

            print("\033[1;31mValor excede o limite da conta.Por favor, tente novamente com um outro valor.\033[m")

            return

        # adiciona o valor a ser depositado à conta
        self.saldo += valor_a_ser_depositado

        print(f"\033[1;32mValor de R${valor_a_ser_depositado:.2f} depositado na conta com sucesso.\nAgora, o saldo da sua conta é de R${self.saldo:.2f}\033[m")



    def pagar_alguem(self, valor_a_ser_pago:float)->None:
        '''-> Paga alguém (o saldo da conta é decrementado)

        Parâmetros:

            valor_a_ser_pago(float): valor a ser pago a pessoa
            return: sem retorno
        '''

        # verifica se o valor a ser pago é superior ao saldo da conta
        if valor_a_ser_pago > self.saldo:

            print("\033[1;31mVocê não tem saldo o suficiente em sua conta.Por favor, considere depositar em sua conta.\033[m")

            return
        
        # decrementa  o saldo da conta pela quantidade que deve ser paga a pessoa
        self.saldo -= valor_a_ser_pago

        print(f"\033[1;32mValor de R${valor_a_ser_pago:.2f} pago com sucesso.")




