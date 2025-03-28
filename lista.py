
import os

def exibir_estrutura(diretorio, nivel=0):
    for item in os.listdir(diretorio):
        caminho = os.path.join(diretorio, item)
        # Indentação para a hierarquia
        print("  " * nivel + "|-- " + item)
        if os.path.isdir(caminho):  # Se for uma pasta, chama a função recursivamente
            exibir_estrutura(caminho, nivel + 1)

# Caminho inicial para seu projeto
diretorio_projeto = "d:/Estudos/SuporteMestreDeMesa"
exibir_estrutura(diretorio_projeto)