import csv
import pandas as pd
import requests
import sys


# Parte IV
def loadSaveURLData(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("datos.csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            lines = response.text.split('\n')

            for line in lines:
                columns = line.split(',')
                csv_writer.writerow(columns)

        print("Archivo CSV guardado exitosamente.\n")
    else:
        print("Error al descargar la respuesta. Código de estado:", response.status_code)


# Parte V
def cleanPrepare(datos):
    print("Limpieza y preparación de los Datos: \n")
    # 1. Verificar que no existan valores faltantes
    if datos.isna().any().any():
        print("-     Existen valores faltantes en el DataFrame.")
        print("-     Borrando filas con datos faltantes...\n")
        data.dropna(inplace=True)
    else:
        print("-     No hay valores faltantes en el DataFrame.\n")
    
    # 2. Verificar que no existan filas repetidas
    if datos.duplicated().any():
        print("-     Existen filas duplicadas en el DataFrame.\n")
        print("-     Borrando filas duplicadas...\n")
        datos.drop_duplicates(inplace=True)
    else:
        print("-     No hay filas duplicadas en el DataFrame.\n")

    # 3. Verificar si existen valores atípicos y eliminarlos
    Q1 = datos.quantile(0.25)
    Q3 = datos.quantile(0.75)
    IQR = Q3 - Q1
    datos = datos[~((datos < (Q1 - 1.5 * IQR)) | (datos > (Q3 + 1.5 * IQR))).any(axis=1)]

    # 4. Crear una columna que categorice por edades
    datos['Age_Category'] = datos['age'].apply(categorizeAge)

    # 5. Guardar el resultado como csv
    datos.to_csv("cleanData.csv")

    print("\n\nArchivo CSV guardado exitosamente.\n")
    

def categorizeAge(age):
    if age >= 0 and age <= 12:
        return 'Niño'
    elif age >= 13 and age <= 19:
        return 'Adolescente'
    elif age >= 20 and age <= 39:
        return 'Joven adulto'
    elif age >= 40 and age <= 59:
        return 'Adulto'
    else:
        return 'Adulto mayor'
    

# url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
url = sys.argv[1]
loadSaveURLData(url)

data = pd.read_csv("datos.csv")
cleanPrepare(data)