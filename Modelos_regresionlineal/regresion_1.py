import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Cargar el archivo CSV
df = pd.read_csv("../Datasets_preprocesados\API_SL.UEM.1524.ZS_DS2_en_csv_v2_76240_preprocesado.csv")

# Variables
X = df["Año"].values
y = df["Valor"].values

# Separar en training y test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Probar modelos polinómicos de grado 1 a 5 en el conjunto de entrenamiento
bic_scores = []
models = []
potencias = range(1, 6)

for p in potencias:
    X_poly_train = np.vander(X_train, N=p+1, increasing=True)
    model = sm.OLS(y_train, sm.add_constant(X_poly_train)).fit()
    bic_scores.append(model.bic)
    models.append(model)

# Seleccionar mejor modelo según BIC
mejor_indice = np.argmin(bic_scores)
mejor_potencia = potencias[mejor_indice]
modelo_final = models[mejor_indice]

# Preparar los datos de test con la misma potencia
X_poly_test = np.vander(X_test, N=mejor_potencia+1, increasing=True)
y_pred = modelo_final.predict(sm.add_constant(X_poly_test))

# Métricas de evaluación
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mejor grado polinómico según BIC: {mejor_potencia}")
print(modelo_final.summary())
print("\n--- Métricas de Evaluación ---")
print(f"MAE:  {mae:.4f}")
print(f"MSE:  {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²:   {r2:.4f}")

# Gráfica de predicción vs datos reales
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Datos reales (Test)')
plt.scatter(X_test, y_pred, color='red', label='Predicción', marker='x')
plt.xlabel('Año')
plt.ylabel('Valor')
plt.title(f'Regresión polinómica grado {mejor_potencia} - Evaluación')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Predicción para un año ingresado por el usuario
try:
    anio_input = int(input("\nIntroduce un año para predecir su valor: "))
    X_input = np.vander([anio_input], N=mejor_potencia+1, increasing=True)
    valor_predicho = modelo_final.predict(sm.add_constant(X_input))
    print(f"\nPredicción para el año {anio_input}: {valor_predicho[0]:.4f}")
except ValueError:
    print("⚠️ Por favor ingresa un año válido (número entero).")