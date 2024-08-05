import tabula
import PyPDF2
import re
import fitz  # PyMuPDF
import pdfplumber


with pdfplumber.open('callan_1.pdf') as pdf:

    livro_1=[]

    for i in range(len(pdf.pages)):
        texto = pdf.pages[i]
        texto_negrito = texto.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"])
        # print(clean_text.extract_text())
        texto_negrito=texto_negrito.extract_text().replace('\n', ' ')
        palavras=texto_negrito.split()
        livro_1.append(palavras)
        

