class Navio:


    def __init__(self, quantidade_pessoas, peso_carga, tipo_de_carga="bronze"):

        self.quantidade_pessoas = quantidade_pessoas
        self.peso_da_carga = peso_carga
        self.tipo_da_carga = tipo_de_carga


    
    def __str__(self):

        print(f'''<<< Informações do navio:\nNúmero de pessoas: {self.quantidade_pessoas}\nPeso da carga: {self.peso_da_carga}\nTipo da carga: {self.tipo_da_carga}''')


