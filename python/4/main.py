from conta import ContaBancaria


# cria um objeto conta1 a partir da classe ContaBancaria
conta1 = ContaBancaria("Mateus", 20501, 20000)

# printa os dados na tela
print(conta1.titular, conta1.saldo)

# deposita (ou pelo menos tenta) um valor de R$15000
conta1.depositar(15000)

# printa os dados na tela
print(conta1.titular, conta1.saldo)


# paga alguém no valor de R$11111,00
conta1.pagar_alguem(11111)


# Imprime o saldo
print(conta1.saldo)

# transfere uma quantidade de R$18000 à conta de uma pessoa (ou pelo menos tenta)
conta1.pagar_alguem(18000)

# deposita R$10000,00 na conta
conta1.depositar(10000)

# imprime o saldo
print(conta1.saldo)
