from classes import *
from funcs import *


info_navio = define_navio()


navio1 = Navio(info_navio["quantidade de pessoas"], info_navio["peso da carga"], info_navio["tipo do minério"])


navio1.__str__()


peso_dos_minerios = determina_peso_do_minerio(navio1.peso_da_carga, navio1.quantidade_pessoas)

print(peso_dos_minerios)


if peso_dos_minerios >= 100000:


    print("Vale a pena saquear o navio")

else:

    print("Não vale a pena saquear o navio")


