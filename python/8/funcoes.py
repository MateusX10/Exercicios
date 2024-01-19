def menu()-> None:
    '''-> Exibe o menu de opções na tela

        Parâmetros:

            return: sem retorno
    '''

    print('''Menu de opções:
\n[ 1 ] - Adicionar livro à biblioteca\n[ 2 ] - Emprestar livro\n[ 3 ] - Devolver livro\n[ 4 ] - Visualizar lista de livros\n[ 5 ] - Livro emprestado\n[ 6 ] - Exibe informações de um livro\n[ 7 ] - Sair do programa ''')
    


def linha(tamanho_linha)-> None:
    '''-> Exibe uma linha na tela de tamanho "t"

        Parâmetros:

            tamanho_linha(int): o tamanho da linha a ser exibida na tela
            return: sem retorno
    '''

    print("-=" * tamanho_linha)




def title(texto)-> None:
    '''-> Exibe um título na tela

        Parâmetros:

            texto(str): texto a ser exibido no título
            return: sem retorno
    '''
    

    tamanho_linha = len(texto)

    linha(tamanho_linha)
    print(texto.center(tamanho_linha * 2))
    linha(tamanho_linha)


def quebraLinha(quantidadeDeQuebras)-> None:
    '''-> Faz a quebra de linha

        Parâmetros:

            quantidadeDeQuebras(int): quantidade de quebras de linha que serão feitas
            return: sem retorno
    '''

    for quebra in range(0, quantidadeDeQuebras):

        print("\n")


def leiaInt(texto)-> int:
    '''-> Lê e valida um número inteiro lido pelo teclado
        Parâmertros:

            texto(str): texto personalizado a ser exibido ao usuáro na entrada de dados
            return: retorna o número inteiro  validado
    '''


    from sys import exit


    # lê o número
    while True:

        try:

            numero = int(input(texto))

        # exceções que possam vir a ocorrer
        except (NameError, ValueError):

            print("\033[1;31mTivemos um problema com o tipo de dados que você digitou.\033[m")


        except (KeyboardInterrupt):


            print("\033[1;31mEntrada de dados interrompida pelo usuário.\033[m")

            exit(1)


        except Exception as tipo_da_excecao:

            print(f"\033[1;31mOcorreu uma exceção: {tipo_da_excecao}")


        # deu certo, retorne o número
        else:


            return numero



def le_informacoes_do_livro()-> dict:
    '''-> Lê as informações do livro, definindo o título, autor, ano de publicação e quantidade disponível desse livro.

        Parâmetros:

            return: retorna um dicionário contendo as informações do livro na seguinte nomenclatura: "{titulo: titulo do livro, autor: autor do livro, ano_publicação: ano de publicação do livro, quantidade_disponivel: quantidade disponível do livro}
    '''

    # lê e define o título do livro
    while True:

        titulo = str(input("Título do livro: ")).strip().capitalize()

        if len(titulo) >= 3:

            break
        print("\033[1;31mTítulo inválido.Por favor, insira um título com um mínimo de 3 caracteres.\033[m")


    # lê e define o autor do livro
    while True:


        autor = str(input("Autor: ")).strip().capitalize()


        if len(autor) >= 3:

            break

        print("Autor inválido.Por favor, forneça um nome de autor com um mínimo de 3 caracteres.\033[m")


    # lê e define o ano de publicação
    ano_publicao = leiaInt("Ano de publicação: ")



    # lê e define a quantidade disponível
    while True:


        quantidade_disponivel = leiaInt("Quantidade disponível: ")

        if quantidade_disponivel >= 1:

            break
        
        print("\033[1;31mOpção inválida.Tente novamente.\033[m")


    # dicionário contendo as informações do livro
    return {"título": titulo, "autor": autor, "ano de publicação": ano_publicao, "quantidade disponível": quantidade_disponivel, }
