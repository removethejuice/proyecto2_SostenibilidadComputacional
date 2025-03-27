import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ========== CARGA Y PREPROCESAMIENTO ==========

df = pd.read_csv(r"C:\Users\pablo\Desktop\proyecto2_SostenibilidadComputacional\Datasets_preprocesados\Evolución de los homicidios de hombres y muertes violentas de mujeres y femicidio por sexo de la víctima, 2011-2022 (tasa por 100.000 habitantes).csv")

# ========== ESTADÍSTICAS BÁSICAS ==========
# Mostrar las estadísticas básicas (media, mediana, min, max, etc.)
print("\n--- Estadísticas Básicas ---")
print(df.describe())

# ========== CÁLCULOS DE MEDIA Y MEDIANA ==========
mean_homicidios = df["Homicidios de hombres"].mean()
median_homicidios = df["Homicidios de hombres"].median()

mean_femicidios = df["Muertes violentas de mujeres y femicidios"].mean()
median_femicidios = df["Muertes violentas de mujeres y femicidios"].median()

print(f"\nMedia de Homicidios de hombres: {mean_homicidios:.2f}")
print(f"Mediana de Homicidios de hombres: {median_homicidios:.2f}")

print(f"\nMedia de Muertes violentas de mujeres y femicidios: {mean_femicidios:.2f}")
print(f"Mediana de Muertes violentas de mujeres y femicidios: {median_femicidios:.2f}")

# ========== GRAFICAS ==========
# Gráfico 1: Scatter plot de Homicidios de hombres vs. Año
plt.figure(figsize=(10, 6))
plt.scatter(df['Año'], df['Homicidios de hombres'], color='blue', label='Homicidios de hombres')
plt.plot(df['Año'], df['Homicidios de hombres'], color='blue', linestyle='--')
plt.xlabel('Año')
plt.ylabel('Homicidios de hombres')
plt.title('Evolución de los Homicidios de hombres (2011-2022)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 2: Scatter plot de Muertes violentas de mujeres y femicidios vs. Año
plt.figure(figsize=(10, 6))
plt.scatter(df['Año'], df['Muertes violentas de mujeres y femicidios'], color='red', label='Muertes violentas de mujeres y femicidios')
plt.plot(df['Año'], df['Muertes violentas de mujeres y femicidios'], color='red', linestyle='--')
plt.xlabel('Año')
plt.ylabel('Muertes violentas de mujeres y femicidios')
plt.title('Evolución de las Muertes violentas de mujeres y femicidios (2011-2022)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 3: Scatter plot comparando ambas variables
plt.figure(figsize=(10, 6))
plt.scatter(df['Año'], df['Homicidios de hombres'], color='blue', label='Homicidios de hombres')
plt.scatter(df['Año'], df['Muertes violentas de mujeres y femicidios'], color='red', label='Muertes violentas de mujeres y femicidios')
plt.xlabel('Año')
plt.ylabel('Valor')
plt.title('Comparación de Homicidios de hombres y Muertes violentas de mujeres y femicidios')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ========== MATRIZ DE CORRELACIÓN ==========
plt.figure(figsize=(8, 6))
correlation_matrix = df.corr()  # Corregido: usar 'df' en lugar de 'data'
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matriz de Correlación')
plt.show()