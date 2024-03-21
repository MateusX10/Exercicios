from classes import *
from funcs import *
import os

# Verifica se há arquivos na lista de arquivos retornadas da pasta "arquivo de texto/" através da função "listdir()"
if not os.listdir("novo/arquivo de texto"):
    
    nomeDoArquivo = ''


    while not nomeDoArquivo:

        nomeDoArquivo = str(input("Nome do arquivo: ")).strip()




    arquivo_texto1 = ArquivoDeTexto(nomeDoArquivo)


else:

    nomeDoArquivo = os.listdir("novo/arquivo de texto")[0]


    arquivo_texto1 = ArquivoDeTexto(nomeDoArquivo)



while True:


    opcoes_menu = [1, 2, 3, 4, 5, 6, 7, 8]

    menu()


    while True:


        escolhaUsuario = leiaInt("Sua escolha: ")


        if escolhaUsuario in opcoes_menu:

            break

        print("\033[1;31mOpção inválida.Tente novamente.\033[m")


    if escolhaUsuario == 1:


        linhaDeTexto = ''


        while len(linhaDeTexto) == 0:
            linhaDeTexto = str(input("Linha de texto a ser adicionada: ")).strip()


        arquivo_texto1.adicionar_linha_de_texto(linhaDeTexto)
        




    elif escolhaUsuario == 2:

        arquivo_texto1.lerArquivo()


    elif escolhaUsuario == 3:


        pass


    elif escolhaUsuario == 4:

        pass


    elif escolhaUsuario == 5:


        pass


    elif escolhaUsuario == 6:


        pass


    elif escolhaUsuario == 7:


        pass



    elif escolhaUsuario == 8:

        pass




    