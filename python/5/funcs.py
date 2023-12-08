def soma_multiplos_de_3_ou_5_do_numero_passado(numero:int)->int:
    '''-> Soma todos os números múltiplos de 3 e de 5 dos descendentes do número passado como parâmetro (o número passado como parâmetro também é incluído)

        Parâmetro:

            numer(int): número a ser somado o múltiplo de 3 e 5 seu e de seus descendentes.
            return: retorna a soma dos múltiplos
    '''



    soma = 0

    # faz um laço fot que itera sobre o número passado e seus descendentes, somando os números múltiplos de 3 e 5
    for numero_descendente in range(numero, 2, -1):


        if numero_descendente % 3 == 0 or numero_descendente % 5 == 0:

            soma += numero_descendente

    return soma


