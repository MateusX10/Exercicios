def find_outlier(lista_numeros):
    '''-> Retorna o único valor inteiro par ou ímpar da lista

        Parâmetros:

            lista_numeros(list): lista de números a ser verificada
            return: retorna o único valor inteiro ímpar ou par


        Exemplos:

            Lista de entrada: [1, 2, 3, 5, 7, 9]

            Saída: 2


            Lista de entrada: [30, 32, 36, 40, 1]

            Saída: 1


            Lista de entrada: [1, 2, 3, 4, 6, 10, 30, 101]

            Saída: None 
    '''
    
    quantidade_par = list()
    quantidade_impar = list()
    
    # varre a lista "numero" em busca de valores pares ou ímpares únicos
    for numero in lista_numeros:
        
        #  número atual da lista é par
        if numero % 2 == 0:
            
            quantidade_par.append(numero)
            

        # número atual da lista é ímpar
        else:
            
            quantidade_impar.append(numero)
            
    # verifica se há um único valor par na lista    
    if len(quantidade_par) == 1:
        
        # se sim, então o número é retornado
        return quantidade_par[0]
    
    # verifica se há um único valor ímpar na lista
    elif len(quantidade_impar) == 1:
        

        # se sim, o único valor ímpar é retornado
        return quantidade_impar[0]
    
    # nesse caso, não há nem um único valor par nem um único ímpar, é uma mistura de vários valores pares e ímpares ou a ausência de algum 
    else:
        
        
        return None
        
        