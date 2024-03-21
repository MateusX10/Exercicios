from funcs import *
from arquivos import *
from sys import exit



if not arquivo_existe:

    criarArquivo()


opcoes_menu = [1, 2, 3, 4, 5]


titulos_menu = ["Adicionar pessoa", "Ver pessoas",
                 "Editar pessoa", "Excluir pessoa",
                   "Sair"]


while True:


    menu()


    while True:


        escolhaUsuario = leiaInt("Sua escolha: ")


        if escolhaUsuario in opcoes_menu:

            break

        print("\033[1;31mEscolha não existe no menu.\033[m")


    
    titulo(titulos_menu[escolhaUsuario - 1])



    if escolhaUsuario == 1:

        while True:
            nomePessoa = str(input("Nome da pessoa: ")).strip().capitalize()

            if len(nomePessoa) < 3:

                print("\033[1;31mNome inválido.Por favor, tente novamente.\033[m")

                continue


            break


        adicionar_pessoa(nomePessoa)

                


    elif escolhaUsuario == 2:


        lerArquivo()



    elif escolhaUsuario == 3:


        lista_pessoas = retorna_lista_de_pessoas()


        lerArquivo()


        while True:

            pessoa_a_ser_alterada = leiaInt("Editar qual pessoas? ")


            if (pessoa_a_ser_alterada - 1) in list(range(len(lista_pessoas))):

                break

            print("\033[1;31mpessoa inexistente.\033[m")


        while True:


            nova_pessoa = str(input("Nova pessoa: ")).strip().capitalize()

            if len(nova_pessoa) >= 3:

                break


            print("\033[1;31mPessoa inexistente.\033[m")



        novos_dados = editar_pessoa(pessoa_a_ser_alterada, nova_pessoa)


        atualiza_alteracoes(novos_dados)


    elif escolhaUsuario == 4:


        lista_pessoas = retorna_lista_de_pessoas()

        lerArquivo()


        while True:

            pessoa_a_ser_excluida = leiaInt("Excluir qual pessoas?")


            if (pessoa_a_ser_excluida - 1) in list(range(len(lista_pessoas))):


                break
            
            print("\033[1;31mPessoa inexistente.\033[m")



        
        novos_dados = exclui_pessoa(pessoa_a_ser_excluida)


        atualiza_alteracoes(novos_dados)


    elif escolhaUsuario == 5:

        exit(0)


    
    else:


        print("\033[1;31mOpção inexistente.\033[m")


        continue






