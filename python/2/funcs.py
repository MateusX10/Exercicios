def leiaStr(mensagem):
    '''-> Lê uma string pelo teclado

        Parâmetros:

            mensagem(str): mensagem a ser exibida na entrada de dados
            return: retorna a string validada
    '''

    while True:

        try:
            string = str(input(mensagem)).strip()

        # exceção onde o usuário interrompeu a entrada de dados
        except (KeyboardInterrupt):

            print("\033[1;31mEntrada de dados interrompida pelo usuário.033[m")

        # valida todas as demais exceções que possam vir a ocorrer
        except Exception as exp:

            print(f"\033[1;31mExeceção = {exp}\033[m")

        # deu tudo certo
        else:
            # verifica se string não é só um "nada", um espaço vazio
            if string == "":

                print("\033[1;31mDigite ao menos um dígito.\033[m")
                continue

            return string






def separa_string_em_pares(string):
    '''-> Separa uma string em pares formando no final uma lista, na qual cada item da lista é um par  de caracteres
    '''

    # string onde estará a string separada por pares
    string_separada_em_pares = list()

    # lista temporária onde serão armazenados os pares da iteração atual (os pares atuais)
    lista_temporaria = list()
    
    # percorre a lista de pares inteira
    for posicao,caractere in enumerate(string):
        
        # armanzena na lista "lista_temporaria" um dos caracteres do par atual
        lista_temporaria.append(caractere)


        # verifica se a posição do caracter atual é ímpar ou se é o último caracter da string.Caso seja, isso indica que a "lista_temporaria" deve ser adicionada a "stirng_separada_em_pares"
        if posicao % 2 == 1 or posicao == len(string) - 1:

            # verifica se o elemento atual da lista é o último caractere da lista.Se for, isso indica que ele está sem um par, logo é adicionado um "_" junto dele para assim os torarem um par
            if posicao == len(string) - 1:

                lista_temporaria.append("_")


            # adiciona os elementos da "lista_temporaria" à lista "string_separada_em_pares", ou seja, os pares de caracteres atuais estão sendo adicionados à lista de pares
            string_separada_em_pares.append(lista_temporaria[:])

            # limpa a lista temporaria para assim se evitar o acúmulo de itens
            lista_temporaria.clear()    

    
    return string_separada_em_pares





