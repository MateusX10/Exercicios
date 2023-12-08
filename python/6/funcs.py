def conta_entre(numero_inicial, numero_final):
    '''-> Conta a soma dos valores entre o número inicial e o final

        Parâmetros:

            numero_inicial(int): número inicial do intervalo
            numero_final(int): número final do intervalo   
            return: retorna a soma dos valores entre o intervalo do número_inicial e o número_final
    '''                        

    # verifica se o número é uma instância de str.Caso seja, ambos os numero_inicial e numero_final são definidos como 0.
    if isinstance(numero_inicial, str) or isinstance(numero_final, str):

        numero_inicial = numero_final = 0

    # verifica se o numero_inicial e o numero_final são instâncias de float.Caso sejam, é feito um casting para int
    numero_inicial = int(numero_inicial) if isinstance(numero_inicial, float) else numero_inicial

    numero_final = int(numero_final) if isinstance(numero_final, float) else numero_final

    soma = 0
    

    # verifica se  o numero_inicial é igual ao numero_final.Caso seja, é retornado o numero_inicial, pois não há valores entre eles, somente eles mesmos.
    if numero_inicial == numero_final:

        return numero_inicial

    # itera cada número dentro do intervalo e incrementa a soma deles na variável soma
    for valor in range(numero_inicial, numero_final + 1):

        soma += valor


    return soma

        
