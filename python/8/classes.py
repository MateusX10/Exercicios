class Livro:
    '''-> Classe que representa um livro


    '''

    def __init__(self, titulo, autor, ano_publicacao, quantidade_disponivel):
        '''-> Construtor da classe "Livro"
        '''

        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.quantidade_disponivel = quantidade_disponivel


    def __str__(self):
        '''-> Exibe informações do livro
        '''

        return f"{self.titulo}\nAutor: {self.autor}\nAno de publicação: {self.ano_publicacao}\nQuantidade disponível: {self.quantidade_disponivel}"

    
    @classmethod
    def criar_livro(cls, titulo, autor, ano_publicacao, quantidade_disponivel):
        '''->  adiciona/cria um livro, criando um objeto desse livro a partir do construtor

            Parâmetros:

                titulo(str): título do livro
                autor(str): nome do autor do livro
                ano_publicacao(int): ano de publicação do livro
                quantidade_disponivel(int): quantidade disponível do livro
                return: uma nova instância da classe livro a partir das informações fornecidades sobre o livro
        '''

        return cls(titulo, autor, ano_publicacao, quantidade_disponivel)




class Biblioteca:
    '''-> Classe que representa uma biblioteca
    '''

    def __init__(self):
        '''-> Construtor da classe biblioteca

            Parâmetros:
                return: sem retorno
        '''

        # lista de livros que há na biblioteca
        self.lista_livros = []

    
    def adicionar_livros_a_biblioteca(self, livro, gravar_no_arquivo=True):
        '''-> Adiciona livros à bviblioteca

            Parâmetros:

                livro(object): livro a ser adicionado a biblioteca
                return: sem retorno
        '''

        from arquivos import escreveNoArquivo

        # adiciona o livro à biblioteca
        self.lista_livros.append(livro)

        if gravar_no_arquivo:

            escreveNoArquivo("biblioteca.txt", livro)


    
    def emprestar_livro(self, posicao_do_livro):
        '''-> Empresta um livro da biblioteca

            Parâmetros:

                posicao_do_livro(int): posição do livro.Usado para obter o livro a ser emprestado e para remover o livro da biblioteca assim que emprestado
        '''

        from arquivos import escreveNoArquivo, verificaSeTamanhoDoArquivo_e_menor_que_3, exclui_livro_do_arquivoBiblioteca


        # chama a função que verifica o tamanho do arquivo de texto "livros_emprestados.txt" para assim ver se o usuário emprestou mais de 3 livros ou não.Isso servirá para validar se o usuário pode ou não emprestar mais livros)
        usuario_pode_emprestar_mais_livros_ou_nao = verificaSeTamanhoDoArquivo_e_menor_que_3()

        # verifica se o usuário pode emprestar mais livros ou não
        if usuario_pode_emprestar_mais_livros_ou_nao:   

            # obtém o livro a ser emprestado

            livro_emprestado = self.lista_livros[posicao_do_livro]

            # escreve/adiciona o livro à lista de livros emprestados
            escreveNoArquivo("livros_emprestados.txt", livro_emprestado)

            # remove o livro emprestado da lista de livros da biblioteca
            self.lista_livros.pop(posicao_do_livro)


            exclui_livro_do_arquivoBiblioteca(posicao_do_livro)

            

        # usuário não pode mais emprestar livro, pois chegou no limite (3 livros no máximo)
        else:

            print("\03[1;31mVocê não pode mais emprestar livros, pois passou do limite (3 livros no máximo)")
            


    def listar_livros(self):
        '''-> Lista os livros da biblioteca

            Parâmetros:

                return: sem retorno
            
        '''

    
        for pos, livro in enumerate(self.lista_livros):

            

            print(f"{pos + 1} - {livro.titulo}")


    def fazBackupDoArquivoParaBiblioteca(self):
        '''-> Pega os livros do arquivo "biblioteca.txt" e adiciona a nossa (objeto) biblioteca

            Parâmetros:

                return: sem retorno
        '''

        with open("biblioteca.txt", "r") as arquivo:

            lista_de_livros = arquivo.readlines()

            for livro in lista_de_livros:
                
                # pega as informações do livro (titulo;autor;ano de publicação;quantidade disponível) e a "splita" (split/divide) transformando em uma lista, já que cada informação do livro é separado por um ";"
                informacoes_do_livro = livro.split(";")

                # pega o título do livro
                titulo_do_livro = informacoes_do_livro[0]

                # pega o autor do livro
                autor_do_livro = informacoes_do_livro[1]

                # pega o ano de publicação do livro
                ano_de_publicacao_do_livro = informacoes_do_livro[2]

                # pega a quantidade disponível do livro
                quantidade_disponivel_do_livro = informacoes_do_livro[3]

                # cria o livro e ,após, o adiciona à biblioteca
                self.adicionar_livros_a_biblioteca(Livro.criar_livro(titulo_do_livro, autor_do_livro, ano_de_publicacao_do_livro, quantidade_disponivel_do_livro), False)

                


    

