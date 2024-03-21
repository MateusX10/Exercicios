def arquivo_existe():


    from os import path


    if path.isfile("pessoas.txt"):

        return True
    

    else:


        return False


def criarArquivo():

    with open("pessoas.txt", "a"):

        pass



def adicionar_pessoa(nomePessoa):

    with open("pessoas.txt", "a") as arquivo:


        arquivo.write(nomePessoa + "\n")



def lerArquivo():

    with open("pessoas.txt", "rt") as arquivo:


        pessoas = arquivo.readlines()


        for posicao, pessoa in enumerate(pessoas):

            print(f"{posicao + 1} - {pessoa}")




def editar_pessoa(posicao_pessoa, nova_pessoa):


    with open("pessoas.txt", "rt") as arquivo:


        pessoas = arquivo.readlines()

        pessoas.pop(posicao_pessoa - 1)

        pessoas.insert(posicao_pessoa - 1, nova_pessoa + "\n")

        return pessoas





def exclui_pessoa(posicao_pessoa):


    with open("pessoas.txt", "r") as arquivo:

        pessoas = arquivo.readlines()


        pessoas.pop(posicao_pessoa - 1)


        return pessoas





def atualiza_alteracoes(novos_dados):


    with open("pessoas.txt", "wt") as arquivo:


        arquivo.writelines(novos_dados)




def retorna_lista_de_pessoas():


    with open("pessoas.txt", "rt") as arquivo:


        pessoas = arquivo.readlines()


        return pessoas



    