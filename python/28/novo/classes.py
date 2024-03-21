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
    "txt", "csv", "json", "xml", "yaml", "ini", "html", "css", "js",
    "py", "java", "cpp", "c", "h", "hpp", "rb", "php", "pl", "sh",
    "bat", "ps1", "exe", "dll", "lib", "obj", "pdb", "so", "dylib",
    "zip", "tar", "gz", "bz2", "rar", "7z", "tar.gz", "tar.bz2", "iso",
    "img", "bin", "cue", "mdf", "nrg", "avi", "mp4", "mkv", "wmv",
    "mp3", "wav", "ogg", "flac", "jpg", "jpeg", "png", "gif", "bmp",
    "tiff", "psd", "ai", "svg", "eps", "pdf", "doc", "docx", "xls",
    "xlsx", "ppt", "pptx"
]



        nome_de_arquivo_dividido = nome.split(".")

        if nome_de_arquivo_dividido[-1] not in lista_extensoes_arquivo:

            nome = "".join(nome_de_arquivo_dividido[:-1]) + ".txt"

        self._nome = nome


        
    def __str__(self):

        print(f'''Nome do arquivo de texto: {self.nome}\nTema: {self.tema}''')



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




    def grava_alteracoes_no_arquivo_de_texto(self, novos_dados):


        with open(os.path.join("novo/arquivo de texto", self.nome), "w") as arquivo:


            arquivo.writelines(novos_dados)


    def renomeia_arquivo_de_texto(self, novo_nome):


        antigo_nome = f"novo/arquivo de texto/{self.nome}"


        novo_nome = f"novo/arquivo de texto/{novo_nome}"


        os.rename(antigo_nome, novo_nome)





    def apagarArquivoDeTexto(self):


        os.remove(self.nome)


    def __del__(self):

        try:
            os.remove(self.nome)

        except (FileNotFoundError):

            print("\033[1;31mO arquivo não existe e/ou caminho incorreto.\033[m")


        except (PermissionError):

            print("\033[1;31mVocê não tem permissão para excluir esse arquivo.Por favor, verifique as permissões relacionadas ao arquivo e tente novamente.\033[m")


        except (IsADirectoryError):

            print("\033[1;31mVocê está excluindo um diretório, mas deveria ser um arquivo.\033[m")


        except (OSError):

            print("\033[1;31mOcorreu um problema em seu Sistema Operacional.Por favor, se possível, considere trocar de Sistema Operacional se você possuir dual boot e, se mesmo assim o problema persistir, use outro computador.\033[m")



        else:


            print("\033[1;32mArquivo excluído com sucesso.\033[m")


