def define_navio():

    from random import randint
    from random import choice


    opcoes_de_minerios = ["bronze", "prata", "ouro"]

    quantidade_pessoas = randint(600, 10000)

    peso_da_carga = quantidade_pessoas * randint(65, 110)

    tipo_da_carga = choice(opcoes_de_minerios)

    return {"quantidade de pessoas": quantidade_pessoas, "peso da carga": peso_da_carga, "tipo do minério": tipo_da_carga}


def determina_peso_do_minerio(peso_total, quantidade_de_pessoas):

    peso_dos_minerios = peso_total - (quantidade_de_pessoas * 62)


    return peso_dos_minerios








