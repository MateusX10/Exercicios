from funcs import *


# lê  o número a ser posteriormente convertido em binário
numero = leiaInt("Digite um valor: ")

# chama a função que converte o valor inteiro em binário
numero_convertido_para_binario = converteDeDecimalParaBinario(numero)

print(f"\n-> Valor convertido em binário = {numero_convertido_para_binario}\n")

# Chama a função que conta o número de dígitos "1s" contidos no valor binário
quantidade_de_1s = conta_quantidade_de_digitos_um_contidos_no_valor_binario(numero_convertido_para_binario)

linha()

# imprime mensagem na tela indicando o número de dígitos binário "1s"
print(f"-> O número de dígitos 1s contidos no binário {numero_convertido_para_binario} é {quantidade_de_1s}")

linha()