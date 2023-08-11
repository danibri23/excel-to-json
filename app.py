### esto trae el excel, lo lee y lo convierte a json, sin formatear nada de las celdas, y en Unicode

# import pandas as pd

# # Cargar el archivo Excel
# excel_file = "prueba2.xlsx"
# df = pd.read_excel(excel_file)


# # Convertir a JSON
# json_data = df.to_json(orient="records")


# # Guardar el JSON en un archivo
# with open("final.json", "w") as json_file:
#     json_file.write(json_data)


import pandas as pd
import json

# Cargar el archivo Excel
excel_file = "prueba.xlsx"
df = pd.read_excel(excel_file)

# Limpiar y formatear los nombres de las columnas
new_columns = [
    column.split("\n")[0].strip().lower().replace(" ", "_").replace(".", "")
    for column in df.columns
]
df.columns = new_columns

# Convertir a JSON
data_dict = df.to_dict(orient="records")

# Guardar el JSON en un archivo
with open("final.json", "w", encoding="utf-8") as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False, indent=4)
