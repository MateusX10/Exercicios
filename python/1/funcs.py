def linha(tamanho=30)-> None:
    '''-> Imprime uma linha na tela

        Parâmetros:

            tamanho(int): tamanho da linha a ser exibida
    '''

    print("-=" * tamanho)



def leiaInt(mensagem)-> int:
    '''-> Lê um número inteiro pelo teclado e o valida.


        Parâmetros:

            mensagem(str): mensagem a ser mostrada durante a entrada de dados envolvendo a leitura do número pelo teclado
            return: retorna o número validado
    '''


    while True:

        try:

            numero = int(input(mensagem))

        # execeções relacionadas ao uso de variáveis ou funções inexistentes e a tentativa de converter um tipo em outro tipo quando esse tipo não possui um valor compatível para que possa ser convertido ao outro tipo
        except (NameError, ValueError):

            print("\033[1;31mTivemos um problema com o tipo de dados que você digitou.\033[m")

        # usuário interrompeu a entrada de dados
        except (KeyboardInterrupt):

            print("\033[1;31mEntrada de dados interrompida pelo usuário.\033[m")

        # exceções gerais.
        except Exception as exp:

            print(f"\033[1;31mOcorreu uma exceção = {exp}.\033[m")

        # deu tudo certo, a variável "numero" conseguiu contornar todas as exceções
        else:

            return numero


def converteDeDecimalParaBinario(valor):
    '''-> Converte um valor inteiro em binário

        Parâmetros:

            valor(int): valor a ser convertido em binário
            return: retorna o número convertido em binário.O valor em binário é fatiado, retirando os dois primeiros caracteres
    '''


    return bin(valor)[2:]



def conta_quantidade_de_digitos_um_contidos_no_valor_binario(valor_binario):
    '''-> Conta a quantidade de dígitos binários "1" contidos em um valor binário

        Parâmetros:

            valor_binario(bin): valor binário a ser contado
            return: retorna o número de vezes em que o dígito binário "1" se repete no valor binário "valor_binario"
    '''


    return valor_binario.count("1")