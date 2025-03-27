import pandas as pd
import matplotlib.pyplot as plt

# ========== CARGA Y PREPROCESAMIENTO ==========
# Cargar el archivo CSV (ajusta la ruta si es necesario)
df = pd.read_csv(r"C:\Users\pablo\Desktop\proyecto2_SostenibilidadComputacional\Datasets_preprocesados\Inversión Extranjera Directa por Actividad Económica_preprocesado.csv")

# Verificar la estructura del dataset
print("\n--- Primeras Filas del Dataset ---")
print(df.head())

# Convertir la columna de años a tipo numérico
df.set_index("ACTIVIDAD ECONÓMICA", inplace=True)
df.columns = df.columns.astype(str)  # Asegurar que los años son strings

# ========== ESTADÍSTICAS BÁSICAS ==========
print("\n--- Estadísticas Básicas ---")
print(df.describe())

# ========== GRÁFICOS ==========
plt.figure(figsize=(14, 7))

# Graficar la evolución de la actividad económica por sector
for sector in df.index:
    plt.plot(df.columns, df.loc[sector], marker='o', linestyle='-', label=sector)

plt.xlabel('Año')
plt.ylabel('Variación (%)')
plt.title('Evolución de la Actividad Económica por Sector (2000-2023)')
plt.xticks(rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfico de barras para la variación en los años más recientes (2021-2023)
df_recent = df[['2021 r/', '2022 p/', '2023 p/']]

df_recent.T.plot(kind='bar', figsize=(14, 7), colormap='viridis', width=0.8)
plt.xlabel('Año')
plt.ylabel('Variación (%)')
plt.title('Comparación de Variación Económica por Sector (2021-2023)')
plt.xticks(rotation=0)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
