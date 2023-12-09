def retornaComprimentoDaMenorPalavraDeUmaListaDePalavras(lista_palavras:list)->int:
    '''-> Retorna o comprimento da menor palavra de uma lista de palavras

        Parâmetros:

            lista_palavras(list): lista das palavras
            return: retorna o comprimento da menor palavra da lista
    '''

    # pega a menor palavra da lista de palavras
    menor_palavra = min(lista_palavras, key=len)

    print(menor_palavra)

    return len(menor_palavra)




def leiaStr(mensagem:str)->str:
    '''-> Lê uma string pelo teclado

        Parâmetros:

            mensagem(str): mensagem a ser mostrada na entrada de dados
            return: retorna o comprimento da palavra
    '''

    from sys import exit


    while True:


        try:


            numero = str(input(mensagem))


        except (NameError, ValueError):

            print("\033[1;31mTivemos um problema com o tipo de dados que você digitou.\033[m")

            continue


        except (KeyboardInterrupt):

            print("\033[1;31mEntrada de dados interrompida pelo usuário.\033[m")

            exit(1)


        except Exception as exp:

            print(f"\033[1;31mOcorre uma exceção = {exp}\033[m.")

        else:

            return numero
