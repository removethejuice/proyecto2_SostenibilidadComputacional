import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ========== CARGA Y PREPROCESAMIENTO ==========
# Cargar dataset
df = pd.read_csv(r"C:\Users\pablo\Desktop\proyecto2_SostenibilidadComputacional\Datasets_preprocesados\Evolución de los homicidios de hombres y muertes violentas de mujeres y femicidio por sexo de la víctima, 2011-2022 (tasa por 100.000 habitantes).csv")

# Asumimos:
# columna 0 = Variable dependiente (y), columna 1 = Variable independiente (X)
y = df.iloc[:, 0].values
X = df.iloc[:, 1].values.reshape(-1, 1)

# ========== ENTRENAMIENTO ==========
# Separar en entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Agregar constante para regresión lineal
X_train_const = sm.add_constant(X_train)
X_test_const = sm.add_constant(X_test)

# Entrenar modelo
modelo = sm.OLS(y_train, X_train_const).fit()

# Predecir
y_pred = modelo.predict(X_test_const)

# ========== MÉTRICAS DE EVALUACIÓN ==========
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# ========== SALIDA ==========
print("--- MODELO ENTRENADO ---")
print(modelo.summary())

print("\n--- Métricas de Evaluación ---")
print(f"MAE:  {mae:.4f}")
print(f"MSE:  {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²:   {r2:.4f}")

# ========== GRÁFICA ==========
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='purple', label='Datos reales (Test)')
plt.plot(X_test, y_pred, color='black', label='Predicción')
plt.xlabel('Variable Independiente')
plt.ylabel('Variable Dependiente')
plt.title('Regresión Lineal')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ========== PREDICCIÓN DE NUEVO VALOR ==========
try:
    valor_usuario = float(input("\nIntroduce un valor para la variable independiente: "))
    X_input = np.array([[1, valor_usuario]])  # 1 para la constante (intercepto), el valor ingresado
    prediccion_usuario = modelo.predict(X_input)
    print(f"\n✅ Predicción para el valor {valor_usuario}: {prediccion_usuario[0]:.4f}")
except ValueError:
    print("⚠️ Por favor ingresa un número válido.")
