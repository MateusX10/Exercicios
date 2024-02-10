def remove_hashtag_da_url(url):
    '''-> Remove a hashtag/jogo da velha de uma URL e tudo o que vem após ela

        Parâmetros:

            url(str): url a ser tratada
            return: retorna a url sem a hashtag e o conteúdo posterior a hashtag
    '''

    # verifica se há uma hashtag  na url

    # há uma hashtag
    if "#" in url:

        nova_url_sem_hashtag = url.split("#")[0]

    # não há uma hashtag
    else:

        nova_url_sem_hashtag = url


    return nova_url_sem_hashtag