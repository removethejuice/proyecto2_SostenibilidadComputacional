import pandas as pd
import matplotlib.pyplot as plt

# ========== CARGA Y PREPROCESAMIENTO ==========
# Asegúrate de que el archivo CSV tenga las columnas correctas
df = pd.read_csv(r"C:\Users\pablo\Desktop\proyecto2_SostenibilidadComputacional\Datasets_preprocesados\homicidios_edad_sexo_2011-2022.csv")

# Verificar la estructura del dataframe
print("\n--- Primeras Filas del Dataset ---")
print(df.head())

# ========== ESTADÍSTICAS BÁSICAS ==========
print("\n--- Estadísticas Básicas ---")
print(df.describe())

# ========== CÁLCULO DE PROMEDIOS ==========
mean_hombres = df["Hombres (%)"].mean()
mean_mujeres = df["Mujeres (%)"].mean()

print(f"\nMedia de Hombres (%): {mean_hombres:.2f}")
print(f"Media de Mujeres (%): {mean_mujeres:.2f}")

# ========== GRAFICAS ==========
# Gráfico 1: Distribución de hombres y mujeres por grupo de edad
plt.figure(figsize=(12, 6))
plt.bar(df['Grupo de edad'], df['Hombres (%)'], color='blue', alpha=0.7, label='Hombres')
plt.bar(df['Grupo de edad'], df['Mujeres (%)'], color='pink', alpha=0.7, label='Mujeres')
plt.xlabel('Grupo de edad')
plt.ylabel('Porcentaje')
plt.title('Distribución de Hombres y Mujeres por Grupo de Edad')
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfico 2: Comparación de proporciones entre hombres y mujeres
plt.figure(figsize=(12, 6))
plt.plot(df['Grupo de edad'], df['Hombres (%)'], marker='o', linestyle='-', color='blue', label='Hombres')
plt.plot(df['Grupo de edad'], df['Mujeres (%)'], marker='s', linestyle='-', color='pink', label='Mujeres')
plt.xlabel('Grupo de edad')
plt.ylabel('Porcentaje')
plt.title('Comparación de la Distribución por Género en Diferentes Grupos de Edad')
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
