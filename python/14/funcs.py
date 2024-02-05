def retorna_quadrado_de_cada_digito_do_numero(numero)->int:

    numero_em_string = ''

    numero = str(numero)

    for digito in numero:

        valor = int(digito) ** 2

        numero_em_string += str(valor)


    numero_em_inteiro = int(numero_em_string)

    return int(numero_em_inteiro)