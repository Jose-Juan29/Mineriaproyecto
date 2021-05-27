import tensorflow as tf
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


#Importar datos
sales_df= pd.read_csv("C:/Users/JoseJ/OneDrive/Escritorio/IceCreamData.csv")


# 6) PUEBA ESTADISTICA
print("\n\n\n\t\tPRUEBA ESTADISTICA ")

#HIPOTESIS NULA El empleado le dijo al jefe que el volumen promedio de ventas diarias del producto definitivamente llegaría a 500

#Venta de productos
b= sales_df["Revenue"]
#Tamaño de la muestra
n=len(b)

# Establecer la media de la muestra y la desviación estándar de la muestra
mean, std = b.mean(), b.std(ddof=1)

# Calcular el error estándar
# Si es una prueba Z, dividirá la desviación estándar de la población por el radical n, pero la prueba t se debe a que la desviación
# estándar de la población es desconocida, por lo que se usa la desviación estándar de la muestra

se = std / np.sqrt(n)
# prueba t
t = (mean - 500) / se
print('t estadística es {}'.format(t))
# Valor P
P = stats.t.cdf(t, df= n-1)
print('El valor p es {}'.format(P))

print("\n\n\n\n")


# 8) FORECASTING 

#Prediccion de ingresos en base a la temperatura
#Visualizacion de la correlación entre la temperatura y el ingreso diario
sns.scatterplot(sales_df['Temperature'],sales_df['Revenue'])
plt.ylabel('Ganancia en dolares')
plt.xlabel('Temperatura en grados Celsius')
plt.title('Ganancia generada vs Temperatura')
plt.show()

#Creando set de entrenamiento
X_train = sales_df['Temperature']
y_train = sales_df['Revenue']

#Creando modelo
model= tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units = 1, input_shape = [1]))

model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(0.1),loss = 'mean_squared_error')

#Entrenamiento del modelo

epochs_hist = model.fit(X_train,y_train,epochs=100)

keys = epochs_hist.history.keys()


weights = model.get_weights()

#Prediccion
Temp =24
Revenue =model.predict([Temp])
print('\n\nLa ganancia sera de: ',Revenue)
print("\n\n")

#Grafico de Prediccion
plt.scatter(X_train, y_train, color = 'green')
plt.plot(X_train, model.predict(X_train), color= 'red')
plt.ylabel('Ganancia en dolares')
plt.xlabel('Temperatura en grados Celsius')
plt.title('Ganancia generada vs Temperatura')
plt.show()
