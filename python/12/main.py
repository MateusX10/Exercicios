def accum(palavra):
    '''-> Recebe uma palavra como parâmetro e multiplica cada letra da palavra de acordo com a posição

        Parâmetros:

            palavra(str): palavra a ser multiplicada
            return: retorna  a palavra multiplicada

    
        Exemplo:

            palavra de entrada 1: "abcd"

            retorno: "Aa-Bbb-Cccc-Ddddd"

            palavra de entrada 2: "comida"

            retorno: "Cc-Ooo-Mmmm-Iiiii-Dddddd-Aaaaaaa"
    '''

    
    lista_palavras = []
    
    
    for posicao, string in enumerate(palavra):
        
        pedaco_palavra = string * (posicao + 1)

    
        if posicao == (len(palavra) - 1):

            lista_palavras.append(f"{string.upper()}{pedaco_palavra}")


        else:

            lista_palavras.append(f"{string.upper()}{pedaco_palavra}-")
    
            
    palavra_junta = "".join(lista_palavras)

    print(palavra_junta)


accum("abcd")