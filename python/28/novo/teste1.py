import os


arquivos_e_pastas = os.listdir("novo")

caminho = "novo"


pastas = [os.path.join(caminho, item) for item in arquivos_e_pastas if os.path.isdir(os.path.join(caminho, item))]


nome = "novo/backup"


for pasta in pastas:


    if nome == pasta:

        print("é igual")

print(pastas)