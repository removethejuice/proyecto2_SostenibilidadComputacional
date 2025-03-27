import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

# ========== CARGA Y PREPROCESAMIENTO ==========
# Cargar segundo dataset
df2 = pd.read_csv("../Datasets_preprocesados\data_1742777257_preprocesado.csv")

# Asumimos:
# columna 0 = Value (y), columna 1 = Año (X)
y2 = df2.iloc[:, 0].values
X2 = df2.iloc[:, 1].values.reshape(-1, 1)

# ========== ENTRENAMIENTO Y SELECCIÓN DE MODELO POLINÓMICO ==========
# Separar en entrenamiento y test
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)

# Agregar constante para regresión lineal
X2_train_const = sm.add_constant(X2_train)
X2_test_const = sm.add_constant(X2_test)

# Variables para comparar el BIC
bic_values = []
models = []

# Probar diferentes grados de polinomio
for grado in range(1, 6):  # Probar grados 1 a 5
    # Crear características polinómicas
    poly = PolynomialFeatures(degree=grado)
    X2_train_poly = poly.fit_transform(X2_train)
    X2_test_poly = poly.transform(X2_test)
    
    # Ajustar el modelo con las características polinómicas
    modelo_poly = sm.OLS(y2_train, sm.add_constant(X2_train_poly)).fit()
    
    # Guardar el BIC para cada modelo
    bic_values.append(modelo_poly.bic)
    models.append((grado, modelo_poly))

# Seleccionar el modelo con el menor BIC
best_bic_idx = np.argmin(bic_values)
best_model = models[best_bic_idx][1]
best_degree = models[best_bic_idx][0]

# Predecir usando el mejor modelo
X2_test_poly_best = PolynomialFeatures(degree=best_degree).fit_transform(X2_test)
y2_pred_best = best_model.predict(sm.add_constant(X2_test_poly_best))

# ========== MÉTRICAS DE EVALUACIÓN ==========
mae2 = mean_absolute_error(y2_test, y2_pred_best)
mse2 = mean_squared_error(y2_test, y2_pred_best)
rmse2 = np.sqrt(mse2)
r2_2 = r2_score(y2_test, y2_pred_best)

# ========== SALIDA ==========
print("--- MODELO ENTRENADO CON EL MEJOR POLINOMIO (SEGÚN BIC) ---")
print(best_model.summary())

print("\n--- Métricas de Evaluación ---")
print(f"MAE:  {mae2:.4f}")
print(f"MSE:  {mse2:.4f}")
print(f"RMSE: {rmse2:.4f}")
print(f"R²:   {r2_2:.4f}")
print(f"\nMejor grado del polinomio: {best_degree}")
print(f"BIC del mejor modelo: {bic_values[best_bic_idx]:.4f}")

# ========== GRÁFICA ==========
plt.figure(figsize=(10, 6))
plt.scatter(X2_test, y2_test, color='purple', label='Datos reales (Test)')
plt.plot(X2_test, y2_pred_best, color='black', label=f'Predicción (Grado {best_degree})')
plt.xlabel('Año')
plt.ylabel('Valor')
plt.title(f'Regresión Polinómica - Grado {best_degree}')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ========== PREDICCIÓN DE AÑO ==========
try:
    anio_usuario = int(input("\nIntroduce un año para predecir el valor: "))
    X_input2 = np.array([[1] + [anio_usuario**i for i in range(1, best_degree+1)]])  # Para el grado del polinomio
    prediccion_usuario = best_model.predict(X_input2)
    print(f"\n Predicción para el año {anio_usuario}: {prediccion_usuario[0]:.4f}")
except ValueError:
    print(" Por favor ingresa un año válido (entero).")
