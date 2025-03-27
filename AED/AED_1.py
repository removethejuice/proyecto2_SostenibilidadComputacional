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

# ========== ESTADÍSTICAS BÁSICAS ==========
# Estadísticas descriptivas de las variables
desc_stats_X = pd.Series(X.flatten()).describe()
desc_stats_y = pd.Series(y).describe()

print("--- ESTADÍSTICAS DESCRIPTIVAS ---")
print(f"Estadísticas para la variable independiente (X):")
print(desc_stats_X)
print("\nEstadísticas para la variable dependiente (y):")
print(desc_stats_y)

# Mediana, media, máximo, mínimo de ambas variables
print("\n--- Resumen de las estadísticas básicas ---")
print(f"Media de X: {np.mean(X):.4f}")
print(f"Mediana de X: {np.median(X):.4f}")
print(f"Valor máximo de X: {np.max(X):.4f}")
print(f"Valor mínimo de X: {np.min(X):.4f}")

print(f"Media de y: {np.mean(y):.4f}")
print(f"Mediana de y: {np.median(y):.4f}")
print(f"Valor máximo de y: {np.max(y):.4f}")
print(f"Valor mínimo de y: {np.min(y):.4f}")

# ========== GRAFICA: Scatter Plot ==========
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='purple', label='Datos')
plt.xlabel('Variable Independiente (X)')
plt.ylabel('Variable Dependiente (y)')
plt.title('Relación entre X e y (Scatter Plot)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Histograma para X
plt.figure(figsize=(10, 6))
plt.hist(X, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Variable Independiente (X)')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Variable Independiente (X)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Histograma para y
plt.figure(figsize=(10, 6))
plt.hist(y, bins=30, color='orange', edgecolor='black', alpha=0.7)
plt.xlabel('Variable Dependiente (y)')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Variable Dependiente (y)')
plt.grid(True)
plt.tight_layout()
plt.show()

# ========== MATRIZ DE CORRELACIÓN ==========
# Crear DataFrame con las variables relevantes
df_corr = pd.DataFrame({'X': X.flatten(), 'y': y})
correlation_matrix = df_corr.corr()

# Visualización con un heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matriz de Correlación')
plt.show()
