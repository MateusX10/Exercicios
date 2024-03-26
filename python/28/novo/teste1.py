import os


arquivos_e_pastas = os.listdir("novo/")


pastas = [item for item in arquivos_e_pastas if os.path.isdir(item)]

print(pastas)