import csv
import os
from dotenv import load_dotenv

load_dotenv()

does_not_exist = os.getenv("CSV_HEADER_1")
inbox_full = os.getenv("CSV_HEADER_2")
refused = os.getenv("CSV_HEADER_3")


# Cria uma lista de variaveis para usar no loop
bounces = [does_not_exist, inbox_full, refused]

# Estrutura de dados com listas vazias para cada coluna
def init_data(bounces):
    return {bounce: [] for bounce in bounces}

# Dicionário com as colunas desejadas
slip_data = init_data(bounces)

# Essa parte do codigo é pra abrir o CSV e ler
with open('csv/data.csv', 'r', newline='', encoding='utf-8') as file:            
    file_content = csv.DictReader(file)                                  
    for row in file_content:
        reason = row.get("Motivo do bounce")
        if reason in slip_data:
            slip_data[reason].append({
                "Motivo do bounce": reason,
                "Destinatário": row.get("Destinatário")
            })

# Vai criar um CSV para cada variável
for bounce, data in slip_data.items():
    if bounce:
        with open(f"csv/{bounce}.csv", mode="w", encoding="utf-8", newline="") as file:
            output_writer = csv.DictWriter(file, fieldnames=["Motivo do bounce", "Destinatário"])
            output_writer.writeheader()
            output_writer.writerows(data)

