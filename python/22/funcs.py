def generate_hashtag(s):
    

    frase = s.capitalize()

    nova_frase = ''


    for caracter in frase:

        nova_frase += caracter if caracter.strip() != '' else ''


    frase = nova_frase



    if len(frase) >= 140 or len(frase) <= 0:

        mensagem_hashtag = False


    else:


        try:

            if frase[0] == "#":

                frase = frase[1:]

            mensagem_hashtag = '#' + frase.capitalize()

            
        except (IndexError):

            pass

    return mensagem_hashtag