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


        arquivo_texto1.lerArquivo()


        dados_arquivo_de_texto = arquivo_texto1.retorna_lista_de_dados_do_arquivo_de_texto()

        # obtém uma lista dos índices da lista retornada a partir dos dados do arquivo de texto
        opcoes_numericas_possiveis = list(range(len(dados_arquivo_de_texto)))

        posicao_da_linha_a_ser_modificada = novo_dado = ''


        while True:
            while not posicao_da_linha_a_ser_modificada:


                posicao_da_linha_a_ser_modificada = (leiaInt("Selecione uma opção: ") - 1)


                if posicao_da_linha_a_ser_modificada in opcoes_numericas_possiveis:

                    break

                else:


                    posicao_da_linha_a_ser_modificada = ''



            while not novo_dado:


                novo_dado = str(input("Novo dado a substituir o velho: ")).strip()



            if posicao_da_linha_a_ser_modificada and novo_dado:


                break


            continue




        novos_dados = arquivo_texto1.editar_arquivo(posicao_da_linha_a_ser_modificada, novo_dado)


        arquivo_texto1.grava_alteracoes_no_arquivo_de_texto(novos_dados)





    


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




    