from funcs import retornaComprimentoDaMenorPalavraDeUmaListaDePalavras, leiaStr

lista_de_palavras = list()


# valida cada item a ser adicionado a lista
while True:

    lista_de_palavras.append(leiaStr("Digite um valor: "))

    # valida se o usuário deseja continuar
    while True:
        

        try:
            continuar = str(input("Continuar[S/N]? ")).strip().upper()[0]

        except (IndexError, ValueError, NameError):

            print("\033[1;31mTivemos um problema com o tipo de dados que você digitou.\033[m")

            continue

        except (KeyboardInterrupt):

            print("\033[1;31mUsuário preferiu não informar os dados.\033[m")

            quit()
        
        else:

            if continuar in ["S", "N"]:

                break

            print("\033[1;31mOpção inválida.Por favor, tente novamente.\033[m")


    if continuar =="N":

        break


print(lista_de_palavras)

tamanho_da_menor_palavra = retornaComprimentoDaMenorPalavraDeUmaListaDePalavras(lista_de_palavras)


print(f"O tamanho da menor palavra é {tamanho_da_menor_palavra}")