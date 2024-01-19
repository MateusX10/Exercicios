def verificaSeArquivoExiste(nomeArquivo)-> bool:
    '''-> Verifica se o arquivo de texto existe

        Parâmetros:

            nomeArquivo(str): nome do arquivo a ser verificado se existe
            return: retorna "True" para "arquivo existe"; "False" para "arquivo não existe"
    '''
    import os

    # caminho do arquivo a ser verificado
    caminhoArquivo = os.path.exists(nomeArquivo)


    # o arquivo existe
    if caminhoArquivo:

        return True

    # o arquivo não existe
    else:

        return False



def criarArquivo(nomeArquivo)-> None:
    '''-> Cria o arquivo de texto
        Parâmetros:

            nomeArquivo(str): nome do arquivo de texto a ser criado
            return: sem retorno
    '''

    # cria o arquivo de texto
    with open(nomeArquivo, "a") as arquivo:

        pass



def escreveNoArquivo(nomeArquivo, dado_a_ser_escrito)-> None:
    '''-> Escreve no arquivo de texto

        Parâmetros:

            nomeArquov(str): nome do arquivo de texto a ser escrito o dado
            dado_a_ser_escrito(str): dado a ser escrito no arquivo de texto
            return: sem retorno
    '''

    # abre o arquivo em modo de escrita
    with open(nomeArquivo, "a") as arquivo:

        #
        informacoes_do_livro = f"{dado_a_ser_escrito.titulo};{dado_a_ser_escrito.autor};{dado_a_ser_escrito.ano_publicacao};{dado_a_ser_escrito.quantidade_disponivel}"

        # retira os "\n" anteriores que possam haver nas informações do livro (isso pode ocorrer devido a ter ocorrido mais de um ciclo de emprestar-devolver)
        informacoes_do_livro = informacoes_do_livro.replace("\n", "")

        # escreve as modificações no arquivo
        arquivo.write(f"{informacoes_do_livro}\n")



def le_arquivo(nomeArquivo)-> None:
    '''-> Lê um arquivo de texto, exibindo os livros que há nele

        Parâmetros:

            nomeArquivo(str): nome do arquivo a ser lido
            return: sem retorno
    '''

    # abre o arquivo em modo de leitura
    with open(nomeArquivo, "r") as arquivo:


        # obtém uma array com cada linha do arquivo de texto
        arquivo_linha_a_linha = arquivo.readlines()

        # exibe cada linha da array (exibe os livros)
        for pos, linha_de_arquivo in enumerate(arquivo_linha_a_linha):

            informacoes_do_livro = linha_de_arquivo.split(";")

            titulo_do_livro = informacoes_do_livro[0]

            print(f"{pos + 1} - {titulo_do_livro}")



def verificaSeTamanhoDoArquivo_e_menor_que_3()-> bool:
    '''-> Verifica se tamanho do arquivo é menor do que três

        Parâmetros:

            return: "True" para "arquivo é menor do que três, isto é, o usuário tem menos de 3 livros emprestados; "False" para "o arquivo é maior do que três, o usuário já não pode mais emprestar livros pois alcançou o limite (3)
    '''

    # abre o arquivo "livros_emprestados.txt" em formato de leitura
    with open("livros_emprestados.txt", "r") as arquivo:

        # obtém uma array com cada linha do arquivo
        arquivo_linha_a_linha = arquivo.readlines()


        # usuário emprestou 3 ou menos livros
        if len(arquivo_linha_a_linha) <= 3:

            return True
        
        # usuário emprestou mais de 3 livros
        else:
            return False
        


def lista_livros_emprestados():
    '''-> Lista os livros emprestados

        Parâmetros:

            return: sem retorno
    '''

    # abre o arquivo "livros_emprestados.txt" em modo de leitura
    with open("livros_emprestados.txt", "r") as arquivo:

        # obtém uma array de cada linha do arquivo
        lista_livros = arquivo.readlines()

        # pega cada linha do arquivo com a nomenclatura "título; autor; ano publicação; quantidade disponível" e o splita/separa em uma lista a partir do ";".
        for posicao, livro in enumerate(lista_livros):

            livro = livro.split(";")


            # exibe o título do livro
            print(f"{posicao + 1} - {livro[0]}")


    return lista_livros




def obtem_livro_a_ser_devolvido(posicao_do_livro):
    '''-> Obtém o livro a ser devolvido
        Parâmetros:

            posicao_do_livro(int): posição do livro a ser devolvido no arquivo de texto
            return: retorna o livro a ser devolvido, juntamente com suas informações
    '''


    # obtém o livro a ser emprestado e retira o livro emprestado do arquivo de texto
    with open("livros_emprestados.txt", "r") as arquivo:

        lista_livros_emprestados = arquivo.readlines()

        livro_a_ser_devolvido = lista_livros_emprestados[posicao_do_livro]

        lista_livros_emprestados.pop(posicao_do_livro)


        nova_lista_de_itens_do_arquivo = lista_livros_emprestados

        salva_modificacoes_no_arquivo("livros_emprestados.txt", nova_lista_de_itens_do_arquivo)


        return livro_a_ser_devolvido
    

def salva_modificacoes_no_arquivo(arquivo, novos_itens_do_arquivo)-> None:
    '''-> Salva as modificações no arquivo

        Parâmetros:

            arquivo(str): nome do arquivo a ter as modificações feitas
            novos_itens_do_arquivo(str): novos itens a serem subscritos no arquivo
            return: sem retorno
    '''


    with open(arquivo, "w") as arquivo:

        arquivo.writelines(novos_itens_do_arquivo)



def exclui_livro_do_arquivoBiblioteca(posicao_do_livro_a_ser_excluido):

    with open("biblioteca.txt", "r") as arquivo:

        lista_de_livros_da_biblioteca = arquivo.readlines()


        lista_de_livros_da_biblioteca.pop(posicao_do_livro_a_ser_excluido)

        salva_modificacoes_no_arquivo("biblioteca.txt", lista_de_livros_da_biblioteca)

