import pandas as pd

def preprocess_dataset(input_file, output_file):
    # Cargar el dataset desde la fila 7 (skiprows=6, porque Python indexa desde 0)
    df = pd.read_excel(input_file, skiprows=6)

    # Eliminar las filas después de la fila 16 (mantener solo hasta la fila 16)
    df = df.iloc[:10, :]  # Mantiene desde la fila 7 hasta la 16 (10 filas en total)

    # Guardar el dataset preprocesado
    df.to_csv(output_file, index=False)

    print(f" Preprocesamiento completado. Archivo guardado en: {output_file}")

# Uso del script
input_file = "Datasets_intactos/Inversión Extranjera Directa por Actividad Económica.xlsx"  
output_file = "Datasets_preprocesados/Inversión Extranjera Directa por Actividad Económica_preprocesado.csv" 
preprocess_dataset(input_file, output_file)
