from funcs import *


while True:

    palavra = str(input("Informe uma palavra: ")).strip()

    if len(palavra) >= 3:

        break
    
    print("\033[1;31mPalavra inválida.Por favor, tente novamente.\033[m")


palavra_antes_de_ser_separada = palavra

nova_palavra = separa_palavra_se_houver_letra_maiuscula(palavra)


print(f"A: {palavra_antes_de_ser_separada}\nAtual: {nova_palavra}")



