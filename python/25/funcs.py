def multiplication_table(size):
    '''-> Gera uma lista sizeXsize


        Parâmetros:

            size(int): tamanho da lista
            return: retorna a lista multiplicada

        
        Exemplo:

            Entrada:  3

            Saída: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    '''

    numeros_da_tabela = []

    numeros_da_linha_atual_da_tabela = list()


    for i in range(1, size + 1):

        for j in range(1, size + 1):

            numeros_da_linha_atual_da_tabela.append(i*j)

        numeros_da_tabela.append(numeros_da_linha_atual_da_tabela[:])

        numeros_da_linha_atual_da_tabela.clear()

    
    return numeros_da_tabela