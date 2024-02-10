def something(numero):


    mensagem = ''

    unidade = numero % 10

    mensagem += f"{unidade}"

    if numero >= 10:
        dezena = (numero // 10) * 10

        mensagem += f"+ {dezena}"


    if numero >= 100:

        centena = (numero // 100) * 100

        mensagem += f"+ {centena}"

    if numero >= 1000:

        milhar = (numero // 1000) * 1000

        mensagem = f"+ {milhar}"


    mensagem += f'= {str(numero)}'


    print(mensagem)

