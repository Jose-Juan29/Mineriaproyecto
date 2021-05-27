import numpy as np
from sklearn import datasets, linear_model 
import matplotlib.pyplot as plt 
from scipy import stats
diabetes = datasets.load_diabetes()
print(diabetes)

# 7) MODELOS LINEALES

#Verifico la informacion contenida en el dataset
print("\n\nInformacion en el dataset:")
print(diabetes.keys())
print("\n\n\n")

#Verifico las caracteristicas del dataset
print("\n\nCARACTERISTICAS DEL DATA: \n\n")
print(diabetes.DESCR)
print("\n\n\n")

#Verifico la cantidad de datos que hay en los dataset
print("Cantidad de datos: ")
print(diabetes.data.shape)
print()

#Verifico la información de las columnas
print("Nombres de las columnas: ")
print(diabetes.feature_names)

#Preparar la data regresion lineal 

#Seleccionamos la columna 
X= diabetes.data[:,np.newaxis,9]

#Definimos los datos correspondientes a las etiquetas
y= diabetes.target

#Graficamos
plt.scatter(X,y)
plt.title("DIABETES")
plt.xlabel("Nivel de azucar en sangre")
plt.ylabel("Progresion de la enfermedad un año despues del inicio")
plt.show()

#Implementacion de la regresion lineal 
from sklearn.model_selection import train_test_split

#separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

#Definimos el algortimo a utilizar
lr = linear_model.LinearRegression()

#Entreno el modelo
lr.fit(X_train, y_train)

#Realizamos una prediccion
Y_pred = lr.predict(X_test)

#Graficamos los datos junto con el modelo
plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color= "red", linewidth =3)
plt.title("Regresion lineal DIABETES")
plt.xlabel("Nivel de Azucar en sangre")
plt.ylabel("Progresion de la enfermedad un año despues del inicio")
plt.show()

print("\n\n\n\t\t Datos del modelo regresion lineal")
print("\nValor de la pendiente o coeficiente 'a' : ")
print(lr.coef_)
print("\nValor de la interseccion o coeficiente 'b' : ")
print(lr.intercept_)
print("\nLa ecuacion del modelo es igual a : ")
print("y = ",lr.coef_, "x ", "+" , lr.intercept_)
print("\nPrecision del modelo: ")
print(lr.score(X_train,y_train))
print("\n\n\n")