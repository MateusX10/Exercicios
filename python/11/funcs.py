def separa_palavra_se_houver_letra_maiuscula(palavra):
    '''-> Separa a palavra por espaço se houver uma letra maiúcula nela.A palavra quebrará na letra maiúscula

        Parâmetros:

            palavra(str): palavra a ser separada/quebrada
            return: retorna a palavra separada/quebrada, se for o caso


        Exemplo:

            - Palavra de entrada: "algumaCoisa"
            
            - O retorno será: "alguma Coisa"


    '''


    nova_palavra = ''

    temporario = list()

    for letra in palavra:

        if letra.isupper():
            
            if len(temporario) == 0:
                temporario = palavra.split(letra)

            else:

                temporario = temporario.split(letra)

            temporario.insert(-1, f' {letra}')

    if len(temporario) > 0:

        for pedaco_de_palavra in temporario:


            nova_palavra += f"{pedaco_de_palavra}"


    else:

        nova_palavra = palavra



    return nova_palavra




