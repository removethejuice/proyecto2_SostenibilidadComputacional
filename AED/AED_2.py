import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ========== CARGA Y PREPROCESAMIENTO ==========
# Cargar dataset
df = pd.read_csv(r"C:\Users\pablo\Desktop\proyecto2_SostenibilidadComputacional\Datasets_preprocesados\Evolución de los homicidios de hombres y muertes violentas de mujeres y femicidio por sexo de la víctima, 2011-2022 (tasa por 100.000 habitantes).csv")

# Asumimos:
# columna 0 = Variable dependiente (y), columna 1 = Variable independiente (X)
y = df.iloc[:, 0].values
X = df.iloc[:, 1].values.reshape(-1, 1)

# Crear un DataFrame con las variables para facilitar análisis
data = pd.DataFrame({'X': X.flatten(), 'y': y})

# ========== ESTADÍSTICAS BÁSICAS ==========
# Estadísticas descriptivas de las variables
desc_stats = data.describe()
print("--- ESTADÍSTICAS DESCRIPTIVAS ---")
print(desc_stats)

# Mediana, media, máximo, mínimo de ambas variables
print("\n--- Resumen de las estadísticas básicas ---")
for col in data.columns:
    print(f"Media de {col}: {np.mean(data[col]):.4f}")
    print(f"Mediana de {col}: {np.median(data[col]):.4f}")
    print(f"Valor máximo de {col}: {np.max(data[col]):.4f}")
    print(f"Valor mínimo de {col}: {np.min(data[col]):.4f}\n")

# ========== GRÁFICOS ==========
# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(data['X'], data['y'], color='purple', label='Datos')
plt.xlabel('Variable Independiente (X)')
plt.ylabel('Variable Dependiente (y)')
plt.title('Relación entre X e y (Scatter Plot)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Histograma para X
data['X'].hist(bins=30, color='skyblue', edgecolor='black', alpha=0.7, figsize=(10, 6))
plt.xlabel('Variable Independiente (X)')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Variable Independiente (X)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Histograma para y
data['y'].hist(bins=30, color='orange', edgecolor='black', alpha=0.7, figsize=(10, 6))
plt.xlabel('Variable Dependiente (y)')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Variable Dependiente (y)')
plt.grid(True)
plt.tight_layout()
plt.show()

# ========== MATRIZ DE CORRELACIÓN ==========
plt.figure(figsize=(8, 6))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matriz de Correlación')
plt.show()
