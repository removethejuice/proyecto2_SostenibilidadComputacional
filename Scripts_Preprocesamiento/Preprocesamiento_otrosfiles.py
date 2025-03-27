import shutil
import os

# Definir la carpeta de origen y destino
source_folder = "Datasets_intactos"  # Reemplaza con la carpeta de origen
destination_folder = "Datasets_preprocesados"  # Reemplaza con la carpeta de destino

# Nombres de los archivos específicos a copiar
file_names = ["femicidios_movil_edad-2011-2022.csv", "Evolución de los homicidios de hombres y muertes violentas de mujeres y femicidio por sexo de la víctima, 2011-2022 (tasa por 100.000 habitantes).csv", "homicidios_edad_sexo_2011-2022.csv"]  # Reemplaza con los nombres reales

# Crear la carpeta de destino si no existe
os.makedirs(destination_folder, exist_ok=True)

# Copiar los archivos
for file_name in file_names:
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(destination_folder, file_name)

    # Verificar si el archivo existe antes de copiarlo
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
        print(f" Archivo copiado: {file_name}")
    else:
        print(f" Archivo no encontrado: {file_name}")
