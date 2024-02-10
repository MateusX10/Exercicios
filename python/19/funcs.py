def conta_ocorrencia_de_caracter(palavra):
    '''-> Conta o número de ocorrências de cada caracter em uma frase

        Parâmetros:

            palavra(str): palavra a ser validada
            return: retorna um dicionário com a ocorrência das palavras
    '''


    # forma 1

    ocorrencia_de_cada_caracter = {}




    for caracter in palavra:

        ocorrencia_de_cada_caracter[caracter] =  palavra.count(caracter)


    return ocorrencia_de_cada_caracter


    # forma 2

    #from collections import Counter


    #return Counter(palavra)




        