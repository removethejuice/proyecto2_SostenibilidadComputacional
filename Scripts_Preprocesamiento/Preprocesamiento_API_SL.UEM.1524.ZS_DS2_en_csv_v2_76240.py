import pandas as pd

def preprocess_dataset(input_file, output_file):
    # Cargar el dataset
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
    df.drop(columns=["Country Name", "Country Code", "Indicator Name", "Indicator Code"], inplace=True)
    
    # Transformar el dataset para que los años sean una columna y los valores otra
    df_melted = df.melt(var_name="Año", value_name="Valor")
    
    # Convertir la columna "Año" a tipo numérico para poder filtrar correctamente
    df_melted["Año"] = pd.to_numeric(df_melted["Año"], errors="coerce")
    
    # Filtrar solo los años a partir de 1992
    df_melted = df_melted[df_melted["Año"] >= 1992]
    
    # Guardar el nuevo archivo preprocesado
    df_melted.to_csv(output_file, index=False)
    
    print(f"Preprocesamiento completado. Archivo guardado en: {output_file}")

# Uso del script
input_file = r"Datasets_intactos\API_SL.UEM.1524.ZS_DS2_en_csv_v2_76240.csv" 
output_file = "Datasets_preprocesados/API_SL.UEM.1524.ZS_DS2_en_csv_v2_76240_preprocesado.csv"  
preprocess_dataset(input_file, output_file)
