import os


class ArquivoDeTexto:


    def __init__(self, nome):

        self.nome = nome 


        # cria arquivo


        caminho_da_pasta = "novo/arquivo de texto/"

        # "path.join()" cria o arquivo no caminho da pasta especificado
        with open(os.path.join(caminho_da_pasta, self.nome), "a"):


            pass
    
        

    @property
    def nome(self):

        return self._nome



    @nome.setter
    def nome(self, nome):

        
        lista_extensoes_arquivo = [
    "txt", "csv", "json", "html", "css", "js",
    "py", "java", "cpp", "c","php"
]
        # o arquivo possui uma extensão/formato
        if "." in nome:

            nome_de_arquivo_dividido = nome.rsplit(".")

            if nome_de_arquivo_dividido[-1] not in lista_extensoes_arquivo:

                nome = "".join(nome_de_arquivo_dividido[:-1]) + ".txt"

        # arquivo não possui uma extensão, é um arquivo sem formato
        else:

            nome = f"{nome}.txt"



        self._nome = nome


        
    def __str__(self):

        print(f'''Nome do arquivo de texto: {self.nome}''')



    def arquivo_existe(self):


        caminho_do_arquivo = "novo/arquivo de texto/"


        nome_do_arquivo = self.nome


        arquivo_com_caminho = os.path.join(caminho_do_arquivo, nome_do_arquivo)

        # o caminho/arquivo existe
        if os.path.exists(arquivo_com_caminho):


            return True

        # o arquivo/caminho não existe
        else:


            return False



    def arquivo_vazio(self):


        caminho_completo_do_arquivo = os.path.join("novo/arquivo de texto", self.nome)


        if os.path.getsize(caminho_completo_do_arquivo) == 0:

            return True

        else:

            return False

    def adicionar_linha_de_texto(self, linha_de_texto):


        nome_arquivo = self.nome

        with open(os.path.join("novo/arquivo de texto/", nome_arquivo), "a") as arquivo:


            arquivo.write(linha_de_texto + "\n")


    
    def lerArquivo(self):

        with open(os.path.join("novo/arquivo de texto/", self.nome), "r") as arquivo:

            lista_dados = arquivo.readlines()


            for posicao, linha in enumerate(lista_dados):


                print(f"{posicao + 1} - {linha}")



    
    def retorna_lista_de_dados_do_arquivo_de_texto(self):


        with open(os.path.join("novo/arquivo de texto/", self.nome), "r") as arquivo:


            lista_dados = arquivo.readlines()


            return lista_dados


    def editar_arquivo(self, posicao_da_linha_a_ser_modificada, novo_dado):

        with open(os.path.join("novo/arquivo de texto/", self.nome), "r") as arquivo:

            lista_dados = arquivo.readlines()

            lista_dados.pop(posicao_da_linha_a_ser_modificada)

            lista_dados.insert(posicao_da_linha_a_ser_modificada, f"{novo_dado}\n")


            return lista_dados




    def renomeia_arquivo_de_texto(self, velho_nome_do_arquivo, novo_nome):


        antigo_nome = f"novo/arquivo de texto/{velho_nome_do_arquivo}"


        novo_nome = f"novo/arquivo de texto/{novo_nome}"


        os.rename(antigo_nome, novo_nome)




    def excluir_linha_do_arquivo_de_texto(self, linha_a_ser_excluida):

        with open(os.path.join("novo/arquivo de texto/", self.nome), "r") as arquivo:

            lista_dados = arquivo.readlines()

            lista_dados.pop(linha_a_ser_excluida)


            return lista_dados


    
    def limpar_arquivo(self):

        with open(os.path.join("novo/arquivo de texto", self.nome), "r") as arquivo:

            lista_dados = arquivo.readlines()

            # limpa os dados da lista
            lista_dados.clear()


            return lista_dados



    def grava_alteracoes_no_arquivo_de_texto(self, novos_dados):


        with open(os.path.join("novo/arquivo de texto", self.nome), "w") as arquivo:


            arquivo.writelines(novos_dados)




    def renomear_arquivo_de_texto(self, novo_nome):


        nome_atual = os.path.join("novo/arquivo de texto/", self.nome)


        novo_nome = os.path.join("novo/arquivo de texto/", novo_nome)


        os.rename(nome_atual, novo_nome)



    def apagarArquivoDeTexto(self):
        
        arquivo_com_caminho = f"novo/arquivo de texto/{self.nome}"


        os.remove(arquivo_com_caminho)




