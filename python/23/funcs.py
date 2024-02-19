def pig_it(frase):

    frase =  frase.split()

    new_word = ''

    new_frase = ''


    for palavra in frase:

        if palavra.isalpha():

            new_word = f"{palavra[1:]}{palavra[0]}ya"

        else:

            new_word = palavra

        new_frase += new_word + ' '


    print(new_frase)

    

