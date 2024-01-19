from classes import Livro, Biblioteca
from funcoes import *
from arquivos import le_arquivo, verificaSeArquivoExiste, criarArquivo, lista_livros_emprestados, obtem_livro_a_ser_devolvido, lista_informacoes_de_um_livro
from sys import exit
from time import sleep

# lista dos arquivos de texto.
lista_arquivos_de_texto = ["biblioteca.txt", "livros_emprestados.txt"]


lista_opcoes_do_menu = ["Adicionar livro", "emprestar livro", "devolver livro", "visualizar lista de livros da biblioteca", "visualizar lista de livros emprestados", "exibir informações de um livro", "sair do programa"]

# itera sobre cada arquivo de texto, verificando se o arquivo de texto existe
for arquivo_de_texto in lista_arquivos_de_texto:

    # verifica se o arquivo de texto existe
    if not verificaSeArquivoExiste(arquivo_de_texto):
        
        # se não existir, o arquivo de texto é criado
        criarArquivo(arquivo_de_texto)




# objeto biblioteca, a nossa biblioteca/acervo de livros
biblioteca1 = Biblioteca()

biblioteca1.fazBackupDoArquivoParaBiblioteca()



while True:

    quebraLinha(2)

    # exibe o menu de opções
    menu()

    quebraLinha(1)

    # verifica se a escolha que o usuário fizer é uma opção válida/existente
    while True:
        escolha_usuario = leiaInt("Sua escolha: ")

        if escolha_usuario in [1, 2, 3, 4, 5, 6, 7]:

            break

        print("\033[1;31mOpção inválida.Por favor, tente novamente.\033[m")

    quebraLinha(2)

    title(lista_opcoes_do_menu[escolha_usuario - 1])
    
    sleep(1)

    quebraLinha(2)

    # adicionar livro à biblioteca
    if escolha_usuario == 1:


        # retorna um dicionário contendo o título, autor, ano de publicação e quantidade disponível especificados pelo usuário
        informacoes_do_livro = le_informacoes_do_livro()

        # define o título
        titulo = informacoes_do_livro["título"]

        # define o autor
        autor = informacoes_do_livro["autor"]

        # define o ano de publicação
        ano_publicacao = informacoes_do_livro["ano de publicação"]

        # define a quantidade disponível
        quantidade_disponivel = informacoes_do_livro["quantidade disponível"]

        # adiciona o livro à biblioteca
        biblioteca1.adicionar_livros_a_biblioteca(Livro.criar_livro(titulo, autor, ano_publicacao, quantidade_disponivel))


    # emprestar livro
    elif escolha_usuario == 2:
        

        # lista os livros da biblioteca
        biblioteca1.listar_livros()

        
        # usuário escolhe qual livro emprestar
        while True:

            escolhaUsuario = leiaInt("Emprestar qual livro? ")

            if 0 < escolhaUsuario  <= len(biblioteca1.lista_livros):

                break

            print("\033[1;31mOpção inválida.Por favor, tente novamente.\033[m")

        posicao_do_livro = escolhaUsuario
        
        # empresta o livro de acordo com a posição do livro
        livro_emprestado = biblioteca1.emprestar_livro(posicao_do_livro - 1)


    # devolver livro
    elif escolha_usuario == 3:


        # lista os livros emprestados pelo usuário
        lista_de_livros_emprestados = lista_livros_emprestados()

        # usuário define qual livro a devolver
        while True:

            escolhaUsuario = leiaInt("Devolver qual livro? ")

            if  0 < escolhaUsuario <= len(lista_de_livros_emprestados):

                break

            print("\033[1;31mOpção inválida.Por favor, tente novamente.\033[m")

        
        # Obtém a posição do livro escolhido pelo usuário
        posicao_do_livro = escolhaUsuario - 1

        #  obtém o livro a ser devolvido do arquivo de texto.Será retornado uma string que segue o seguinte padrão: "título do livro; autor; ano de publicação; quantidade disponível"
        livro_a_ser_devolvido = obtem_livro_a_ser_devolvido(posicao_do_livro)

        # cada informação do livro é separada por um ";", logo separamos cada item numa mesma lista
        livro_a_ser_devolvido = livro_a_ser_devolvido.split(";")

        # obtém o título do livro
        titulo  = livro_a_ser_devolvido[0]

        # obtém o autor do livro
        autor = livro_a_ser_devolvido[1]

        # obtém o ano de publicação do livro
        ano_publicacao = livro_a_ser_devolvido[2]

        # obtém quantidade disponível desse livro
        quantidade_disponivel = livro_a_ser_devolvido[3]

        # o livro é readicionado à biblioteca
        biblioteca1.adicionar_livros_a_biblioteca(Livro.criar_livro(titulo, autor, ano_publicacao, quantidade_disponivel))



    # lista os livros da biblioteca
    elif escolha_usuario == 4:

        biblioteca1.listar_livros()

    # lista os livros emprestados pelo usuário
    elif escolha_usuario == 5:

        sleep(1)


        le_arquivo("livros_emprestados.txt")


    elif escolha_usuario == 6:


        arquivos_de_texto = ["biblioteca.txt", "livros_emprestados.txt"]

        print('''[ 1 ] - Biblioteca
[ 2 ] - Emprestado
        ''')

        while True:

            escolhaUsuario = leiaInt("É um livro da biblioteca ou emprestado? ")

            if escolhaUsuario in [1, 2]:

                break

            print("\033[1;31mDigite somente 1 ou 2\033[m")

        arquivo = arquivos_de_texto[escolhaUsuario - 1]

        lista_informacoes_de_um_livro(arquivo)
        

    # sai do programa
    elif escolha_usuario == 7:

        print('\033[1;32mVolte sempre!\033[m')

        exit(0)







