import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

# ========== CARGA Y PREPROCESAMIENTO ==========
# Cargar dataset
df = pd.read_csv(r"C:\Users\pablo\Desktop\proyecto2_SostenibilidadComputacional\Datasets_preprocesados\Evolución de los homicidios de hombres y muertes violentas de mujeres y femicidio por sexo de la víctima, 2011-2022 (tasa por 100.000 habitantes).csv")

# Asumimos:
# columna 0 = Variable dependiente (y), columna 1 = Variable independiente (X)
y = df.iloc[:, 0].values
X = df.iloc[:, 2].values.reshape(-1, 1)

# ========== ENTRENAMIENTO Y SELECCIÓN DE MODELO POLINÓMICO ==========
# Separar en entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Agregar constante para regresión lineal
X_train_const = sm.add_constant(X_train)
X_test_const = sm.add_constant(X_test)

# Variables para comparar el BIC
bic_values = []
models = []

# Probar diferentes grados de polinomio
for grado in range(1, 6):  # Probar grados 1 a 5
    # Crear características polinómicas
    poly = PolynomialFeatures(degree=grado)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    # Ajustar el modelo con las características polinómicas
    modelo_poly = sm.OLS(y_train, sm.add_constant(X_train_poly)).fit()
    
    # Guardar el BIC para cada modelo
    bic_values.append(modelo_poly.bic)
    models.append((grado, modelo_poly))

# Seleccionar el modelo con el menor BIC
best_bic_idx = np.argmin(bic_values)
best_model = models[best_bic_idx][1]
best_degree = models[best_bic_idx][0]

# Predecir usando el mejor modelo
X_test_poly_best = PolynomialFeatures(degree=best_degree).fit_transform(X_test)
y_pred_best = best_model.predict(sm.add_constant(X_test_poly_best))

# ========== MÉTRICAS DE EVALUACIÓN ==========
mae = mean_absolute_error(y_test, y_pred_best)
mse = mean_squared_error(y_test, y_pred_best)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_best)

# ========== SALIDA ==========
print("--- MODELO ENTRENADO CON EL MEJOR POLINOMIO (SEGÚN BIC) ---")
print(best_model.summary())

print("\n--- Métricas de Evaluación ---")
print(f"MAE:  {mae:.4f}")
print(f"MSE:  {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²:   {r2:.4f}")
print(f"\nMejor grado del polinomio: {best_degree}")
print(f"BIC del mejor modelo: {bic_values[best_bic_idx]:.4f}")

# ========== GRÁFICA ==========
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='purple', label='Datos reales (Test)')
plt.plot(X_test, y_pred_best, color='black', label=f'Predicción (Grado {best_degree})')
plt.xlabel('Variable Independiente')
plt.ylabel('Variable Dependiente')
plt.title(f'Regresión Polinómica - Grado {best_degree}')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ========== PREDICCIÓN DE NUEVO VALOR ==========
try:
    valor_usuario = float(input("\nIntroduce un valor para la variable independiente: "))
    X_input = np.array([[1] + [valor_usuario**i for i in range(1, best_degree+1)]])  # Para el grado del polinomio
    prediccion_usuario = best_model.predict(X_input)
    print(f"\n Predicción para el valor {valor_usuario}: {prediccion_usuario[0]:.4f}")
except ValueError:
    print(" Por favor ingresa un número válido.")
