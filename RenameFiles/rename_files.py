# Jairo Fernandes da Silva - 03/08/2017
# Script para renomear arquivos em lote
# Versão 0.2

import os

caminho = input("Digite o caminho para os arquivos....: ")
#prefixo = input("Digite o prefixo para os arquivos....: ")
prefixo = "Entrevista_Desligamento_"

for old_name in os.listdir(caminho):
    path = os.path.join(caminho, old_name)
    if os.path.isdir(path):
        continue
    else:
        new_name = prefixo + old_name
        os.rename(caminho + old_name, caminho + new_name)
        print("O arquivo " + old_name + " foi renomeado para " + new_name)

# print(caminho)
# print(prefixo)
'''
'''
