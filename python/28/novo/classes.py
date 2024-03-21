import os


class ArquivoDeTexto:


    def __init__(self, nome):

        self.nome = nome 


        # cria arquivo


        caminho_da_pasta = "novo/arquivo de texto/"

        # "path.join()" cria o arquivo no caminho da pasta especificado
        with open(os.path.join(caminho_da_pasta, nome), "a"):


            pass



        
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



