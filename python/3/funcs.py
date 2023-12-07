def sort_array(array):

    # dicionário onde conterá os valores pares da array, assim como as chaves representando as suas posições originais da lista
    valores_pares = dict()

    # lista onde conterá os valores ímpares da lista
    valores_impares = list()
    
    # lista final que conterá os ímpares ordenados, assim como os valores pares com suas devidas originais posições
    lista_final = list()
    

    # percorre a array dada, incluindo ao dicionário "valores_pares" os valores pares da lista como os "valores" e suas respectivas chaves sendo as posições que eles ocupavam na lista
    #por exemplo: dada a lista => [2, 3, 5, 8]
    # o dicionário ficará assim => {"0": 2, "3": 8}
    # assim, após os valores pares serem ordenados e adicionados à lista final, basta dar um insert na lista indicando as posições originais dos itens agora contidos no dicionário
    for posicao, valor in enumerate(array):
        
        # valor é par
        if valor % 2 == 0:

            valores_pares[f"{posicao}"] = valor

        # valor é ímpar
        else:

            valores_impares.append(valor)


    valores_impares.sort()

    # adiciona cada item de "valores_pares" à lista "lista_final"
    for valor in valores_impares:

        lista_final.append(valor)

    
    # adiciona os valores pares à lista final.Devemos lembrar que os valores pares devem permanecer com suas posições inalteradas, mesmo após os valores ímpares terem sido ordenados em ordem crescente.Para isso, apenas armazenando a posição a qual pertencia o tal par da lista, basta inserir esse valor par na exata posição na lista final.
    for chave, valor in valores_pares.items():

        lista_final.insert(int(chave), valor)


    print(lista_final)