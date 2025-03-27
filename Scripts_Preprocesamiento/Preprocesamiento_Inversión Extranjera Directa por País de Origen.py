import pandas as pd

def preprocess_dataset(input_file, output_file):
    # Cargar el dataset desde la fila 7 (skiprows=6 porque Python indexa desde 0)
    df = pd.read_excel(input_file, skiprows=6)

    # Mantener solo las filas desde la 7 hasta la 66 (60 filas de datos)
    df = df.iloc[:60, :]

    # Guardar el dataset preprocesado en formato Excel
    df.to_csv(output_file, index=False)

    print(f" Preprocesamiento completado. Archivo guardado en: {output_file}")

# Uso del script
input_file = "Datasets_intactos/Inversión Extranjera Directa por País de Origen.xlsx"  
output_file = "Datasets_preprocesados/Inversión Extranjera Directa por País de Origen_preprocesado.csv" 
preprocess_dataset(input_file, output_file)
