import pandas as pd

def preprocess_dataset(input_file, output_file):
    # Cargar el dataset omitiendo las primeras 5 filas vacías
    df = pd.read_csv(input_file)
    
    # Eliminar espacios extra en los nombres de las columnas
    df.columns = df.columns.str.strip()
    
    # Verificar las columnas del DataFrame
    print("Columnas disponibles:", df.columns)
    
    # Filtrar solo las filas donde "Country Name" sea "Honduras"
    if "Country Name" in df.columns:
        df = df[df["Country Name"] == "Honduras"].copy()
    else:
        print("'Country Name' no se encuentra en las columnas del DataFrame.")
        return
    
    # Eliminar columnas innecesarias
    df.drop(columns=["Country Code", "Indicator Code"], inplace=True)
    
    # Eliminar los años vacíos (1960-1991)
    columns_to_drop = [str(year) for year in range(1960, 1992) if str(year) in df.columns]
    df.drop(columns=columns_to_drop, inplace=True)
    
    # Guardar el nuevo archivo preprocesado
    df.to_csv(output_file, index=False)
    
    print(f"Preprocesamiento completado. Archivo guardado en: {output_file}")

# Uso del script
input_file = r"Datasets_intactos\API_SL.UEM.1524.ZS_DS2_en_csv_v2_76240.csv" 
output_file = "Datasets_preprocesados/API_SL.UEM.1524.ZS_DS2_en_csv_v2_76240_preprocesado.csv"  
preprocess_dataset(input_file, output_file)
