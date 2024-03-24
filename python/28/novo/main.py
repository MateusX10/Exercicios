from classes import *
from funcs import *
import os
from time import sleep
from sys import exit

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

        novo_dado = ''


        posicao_da_linha_a_ser_modificada = 0 # 0 = False


        # 0 = False
        while not posicao_da_linha_a_ser_modificada:

            posicao_da_linha_a_ser_modificada = (leiaInt("Selecione uma opção: ") - 1)


            if posicao_da_linha_a_ser_modificada in opcoes_numericas_possiveis:

                break

            else:


                posicao_da_linha_a_ser_modificada = 0 # 0 = False



        while True:

            novo_dado = str(input("Novo dado a substituir o velho: ")).strip()



            if novo_dado:

                break


        novos_dados = arquivo_texto1.editar_arquivo(posicao_da_linha_a_ser_modificada, novo_dado)


        arquivo_texto1.grava_alteracoes_no_arquivo_de_texto(novos_dados)





    


    elif escolhaUsuario == 4:


        posicoes_numericas_do_arquivo =  list(range(len(arquivo_texto1.retorna_lista_de_dados_do_arquivo_de_texto())))


        arquivo_texto1.lerArquivo()


        while True:


            posicao_da_linha_a_ser_removida = leiaInt("Posição da linha a ser removida: ") - 1


            if posicao_da_linha_a_ser_removida in posicoes_numericas_do_arquivo:


                break


            print("\033[1;31mOpção inexistente.Tente novamente.\033[m")


        novos_dados = arquivo_texto1.excluir_linha_do_arquivo_de_texto(posicao_da_linha_a_ser_removida)


        arquivo_texto1.grava_alteracoes_no_arquivo_de_texto(novos_dados)

        


    elif escolhaUsuario == 5:


        while True:


            print("\033[1;33;41mATENÇÃO!\033[m")

            sleep(1.5)

            print(f'\033[1;43mTodos os dados do arquivo "{arquivo_texto1.nome}" serão apagados.\033[m')

            sleep(2)


            escolhaUsuario = str(input("\033[1;43mProceder mesmo assim [S/N]? \033[m")).strip().upper()[0]


            if escolhaUsuario in ["S", "N"]:

                break


            print("\033[1;31mPor favor, selecione uma opção válida.\033[m")


        
        if escolhaUsuario == "S":


            dados_vazios = arquivo_texto1.limpar_arquivo()


            arquivo_texto1.grava_alteracoes_no_arquivo_de_texto(dados_vazios)


        else:



            print("A exclusão dos dados do arquivo foi cancelada.")


    elif escolhaUsuario == 6:


        

        while True:


            novo_nome = str(input("Novo nome do arquivo de texto: ")).strip()


            if novo_nome:

                break


            print("\033[1;31mO nome do arquivo não pode ficar em branco.\033[m")


        velho_nome_do_arquivo = arquivo_texto1.nome


        arquivo_texto1.nome = novo_nome

        novo_nome = arquivo_texto1.nome
        
        arquivo_texto1.renomeia_arquivo_de_texto(velho_nome_do_arquivo, novo_nome)





    elif escolhaUsuario == 7:


        arquivo_texto1.apagarArquivoDeTexto()



    elif escolhaUsuario == 8:

        exit(0)    




    