import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from scipy.stats import norm

# Cargar el dataset
file_path = "/Datasets_preprocesados/API_SL.UEM.1524.ZS_DS2_en_csv_v2_76240_preprocesado.csv"  # Ajusta según el nombre del archivo subido
df = pd.read_csv(file_path)

# Convertir columnas a tipo numérico por seguridad
df["Año"] = pd.to_numeric(df["Año"], errors="coerce")
df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")

# Eliminar filas con valores nulos
df.dropna(inplace=True)

# Definir la variable independiente (X) y dependiente (y)
X = df["Año"].values.reshape(-1, 1)
y = df["Valor"].values

# Rango de potencias a evaluar
max_degree = 5  # Evaluaremos modelos polinomiales de grado 1 a 5
bic_scores = []

n = len(y)  # Número de datos

for degree in range(1, max_degree + 1):
    # Crear un pipeline con transformación polinómica y regresión lineal
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X, y)

    # Predicciones y cálculo de error cuadrático medio (MSE)
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    
    # Calcular Bayesian Information Criterion (BIC)
    k = degree + 1  # Número de parámetros (coeficientes del polinomio)
    bic = n * np.log(mse) + k * np.log(n)
    bic_scores.append((degree, bic))

# Seleccionar el grado con el menor BIC
best_degree = min(bic_scores, key=lambda x: x[1])[0]

# Entrenar el modelo final con la mejor potencia
best_model = make_pipeline(PolynomialFeatures(best_degree), LinearRegression())
best_model.fit(X, y)
y_best_pred = best_model.predict(X)

# Graficar los resultados
plt.figure(figsize=(8, 5))
plt.scatter(X, y, label="Datos reales", color="blue", alpha=0.6)
plt.plot(X, y_best_pred, label=f"Regresión (grado {best_degree})", color="red", linewidth=2)
plt.xlabel("Año")
plt.ylabel("Valor")
plt.title(f"Regresión Polinómica de grado {best_degree}")
plt.legend()
plt.grid(True)
plt.show()

# Mostrar el mejor grado seleccionado
best_degree
