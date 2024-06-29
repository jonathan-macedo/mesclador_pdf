from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

caminho = "/mnt/c/Users/jonat/OneDrive/Área de Trabalho/graduacao/Banco de Dados/UA01_UA04"

if os.path.exists(caminho):
    lista_arquivos = os.listdir(caminho)
    lista_arquivos.sort()
    print(lista_arquivos)

    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            merger.append(f"{caminho}/{arquivo}")

    nome_arquivo_novo = "Aulas das Unidades 01 até 04.pdf"
    merger.write(nome_arquivo_novo)

else:
    print(f"O caminho {caminho} não foi encontrado")
