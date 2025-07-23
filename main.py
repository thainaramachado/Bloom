import csv
import time 
import os
from dotenv import load_dotenv

load_dotenv()

does_not_exist = os.getenv("CSV_HEADER_1")
inbox_full = os.getenv("CSV_HEADER_2")
refused = os.getenv("CSV_HEADER_3")

# Essa parte do codigo é pra abrir o CSV e ler
with open('csv/data.csv', 'r', newline='') as arquivo:            
    conteudo = arquivo.read()                                   
    print(conteudo)

# for does_not_exist in conteudo:
#     print("Funcionou")

