def amigo(lista_colegas):
    '''-> Define quem deve ser o seu amigo.Para ser um amigo, precisa ter exatamente 4 caracteres

        Parâmetros:

            lista_colegas(list): lista de colegas a ser avaliado
            return: retorna a lista dos seus amigos
    '''

    lista_amigos = [colega for colega in lista_colegas if len(colega) == 4]

    return lista_amigos