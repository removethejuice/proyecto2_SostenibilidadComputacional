import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ========== CARGA Y PREPROCESAMIENTO ==========
# Asumiendo que el archivo CSV está en una ubicación similar a la anterior
df = pd.read_csv(r"C:\Users\pablo\Desktop\proyecto2_SostenibilidadComputacional\Datasets_preprocesados\Violencia_por_grupo_de_edad.csv")

# ========== ESTADÍSTICAS BÁSICAS ==========
# Mostrar las estadísticas básicas (media, mediana, min, max, etc.)
print("\n--- Estadísticas Básicas ---")
print(df.describe())

# ========== CÁLCULOS DE MEDIA Y MEDIANA ==========
mean_delincuencia = df["Delincuencia organizada (%)"].mean()
median_delincuencia = df["Delincuencia organizada (%)"].median()

mean_violencia_intrafamiliar = df["Violencia intrafamiliar (%)"].mean()
median_violencia_intrafamiliar = df["Violencia intrafamiliar (%)"].median()

mean_violencia_sexual = df["Violencia sexual (%)"].mean()
median_violencia_sexual = df["Violencia sexual (%)"].median()

mean_intimo = df["Íntimo (%)"].mean()
median_intimo = df["Íntimo (%)"].median()

print(f"\nMedia de Delincuencia organizada (%): {mean_delincuencia:.2f}")
print(f"Mediana de Delincuencia organizada (%): {median_delincuencia:.2f}")

print(f"\nMedia de Violencia intrafamiliar (%): {mean_violencia_intrafamiliar:.2f}")
print(f"Mediana de Violencia intrafamiliar (%): {median_violencia_intrafamiliar:.2f}")

print(f"\nMedia de Violencia sexual (%): {mean_violencia_sexual:.2f}")
print(f"Mediana de Violencia sexual (%): {median_violencia_sexual:.2f}")

print(f"\nMedia de Violencia íntima (%): {mean_intimo:.2f}")
print(f"Mediana de Violencia íntima (%): {median_intimo:.2f}")

# ========== GRAFICAS ==========
# Gráfico 1: Scatter plot de Delincuencia organizada vs. Grupo de edad
plt.figure(figsize=(10, 6))
plt.bar(df['Grupo de edad'], df['Delincuencia organizada (%)'], color='blue', label='Delincuencia organizada')
plt.xlabel('Grupo de edad')
plt.ylabel('Delincuencia organizada (%)')
plt.title('Porcentaje de Delincuencia organizada por Grupo de edad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 2: Scatter plot de Violencia intrafamiliar vs. Grupo de edad
plt.figure(figsize=(10, 6))
plt.bar(df['Grupo de edad'], df['Violencia intrafamiliar (%)'], color='green', label='Violencia intrafamiliar')
plt.xlabel('Grupo de edad')
plt.ylabel('Violencia intrafamiliar (%)')
plt.title('Porcentaje de Violencia intrafamiliar por Grupo de edad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 3: Scatter plot de Violencia sexual vs. Grupo de edad
plt.figure(figsize=(10, 6))
plt.bar(df['Grupo de edad'], df['Violencia sexual (%)'], color='red', label='Violencia sexual')
plt.xlabel('Grupo de edad')
plt.ylabel('Violencia sexual (%)')
plt.title('Porcentaje de Violencia sexual por Grupo de edad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 4: Scatter plot de Violencia íntima vs. Grupo de edad
plt.figure(figsize=(10, 6))
plt.bar(df['Grupo de edad'], df['Íntimo (%)'], color='purple', label='Violencia íntima')
plt.xlabel('Grupo de edad')
plt.ylabel('Violencia íntima (%)')
plt.title('Porcentaje de Violencia íntima por Grupo de edad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 5: Comparación de todas las variables
plt.figure(figsize=(10, 6))
plt.bar(df['Grupo de edad'], df['Delincuencia organizada (%)'], color='blue', alpha=0.6, label='Delincuencia organizada')
plt.bar(df['Grupo de edad'], df['Violencia intrafamiliar (%)'], color='green', alpha=0.6, label='Violencia intrafamiliar')
plt.bar(df['Grupo de edad'], df['Violencia sexual (%)'], color='red', alpha=0.6, label='Violencia sexual')
plt.bar(df['Grupo de edad'], df['Íntimo (%)'], color='purple', alpha=0.6, label='Violencia íntima')
plt.xlabel('Grupo de edad')
plt.ylabel('Porcentaje')
plt.title('Comparación de diferentes tipos de violencia por Grupo de edad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
