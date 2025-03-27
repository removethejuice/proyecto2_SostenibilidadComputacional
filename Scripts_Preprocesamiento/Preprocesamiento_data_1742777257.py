import pandas as pd

def preprocess_dataset(input_file, output_file):
    # Cargar el dataset
    df = pd.read_excel(input_file)
    
    # Seleccionar solo las columnas "value" y "Años__ESTANDAR"
    df = df[["value", "Años__ESTANDAR"]].copy()
    
    # Guardar el nuevo archivo preprocesado
    df.to_csv(output_file, index=False)
    
    print(f"Preprocesamiento completado. Archivo guardado en: {output_file}")

# Uso del script
input_file = "Datasets_intactos/data_1742777257.xlsx"  
output_file = "Datasets_preprocesados/data_1742777257_preprocesado.csv"  
preprocess_dataset(input_file, output_file)
