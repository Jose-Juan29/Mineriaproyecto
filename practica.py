import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

                                           # 2) ADQUISICION DE LOS DATOS
data = pd.read_csv("C:/Users/JoseJ/OneDrive/Escritorio/data.csv")
print("\n\n\t\t\t\t DATOS \n\n")
print(data)
                                           # 2) LIMPIEZA DE DATOS
#En mi base de datos si aplicaba drop.na() para eliminar las filas con datos inexistentes me iba a eliminar todo
#Porque la columna 'Joined' y 'Loaned From' son contrarias, osea cuando el jugador está prestado en 'Loaned From', muestra a que club está
#Prestado y en 'Joined' esta vacio, y cuando el jugador no está prestado en 'Joined'  esta la fecha y en 'Loaned From' vacio, por eso 
#Para limpiar los datos mejor a esas celdas vacias les puse texto para rellenarlas con la función 'fillna()
df_filtrado = data.fillna({"Joined" : 'Prestado a otro Club', "Loaned From" : 'Permanece en su Club'})

                                            # 4) ESTADISTICAS DESCRIPTIVAS
print("\n\n\t\t\t ESTADISTICAS DESCRIPTIVAS \n\n")                              
print(df_filtrado.describe())

                                           # 3) ANALISIS DE DATOS 
#MUESTRA A LOS JUGADORES QUE TIENEN UNA CALIFICACIÓN MAYOR O IGUAL A 90
print("\n\n\t\t\t JUGADORES CALIFICACION >= 90 \n\n")   
May = df_filtrado[(df_filtrado["Overall"] >= 90)][['Name','Jersey Number','Position','Overall','Nationality','Age','Wage',
                                    'Value','Contract Valid Until']]
print(May)
#MUESTRA A LOS JUGADORES DE NACIONALIDAD FRANCESA QUE TIENEN UNA CALIFICACIÓN MAYOR O IGUAL A 85 Y TIENEN 25 O MENOS AÑOS
print("\n\n\t\t\t JUGADORES FRANCESES CALIFICACION >= 85 Y EDAD <= 25 \n\n")   
Mayymen = df_filtrado[(df_filtrado["Overall"] >= 85) & (df_filtrado["Age"] <= 25) & (df_filtrado["Nationality"] == "France")][['Name','Jersey Number','Position','Overall','Nationality','Age','Wage',
                                    'Value','Contract Valid Until']]
print(Mayymen)
#Función para mostrar los jugadores en base a alguna nacionalidad 'x'
def Pais(x):
    return df_filtrado[df_filtrado['Nationality'] == x][['Name','Overall','Value','Club','Joined','Loaned From']] 
# Muestra los jugadores de nacionalidad Mexicana. 
print("\n\n\t\t\t JUGADORES DE NACIONALIDAD MEXICANA \n\n")   
print (Pais('Mexico'))
# Muestra los jugadores de nacionalidad Brasileña.
print("\n\n\t\t\t JUGADORES DE NACIONALIDAD BRASILEÑA \n\n")   
print (Pais('Brazil'))
#Funcion para mostrar los jugadores en base a un equipo 
def club(x):
    return data[data['Club'] == x][['Name','Jersey Number','Position','Overall','Nationality','Age','Wage',
                                    'Value','Contract Valid Until']]
# Muestra la información relativa de los jugadores del club mexicano Pumas UNAM
print("\n\n\t\t\t PLANTILLA DEL CLUB MEXICANO PUMAS UNAM \n\n")   
print (club('U.N.A.M.'))
print("\n")
                                                   # 10) AGRUPACION DE DATOS
# POR CADA PAIS MUESTRA LA EDAD MAS GRANDE DE ALGUN JUGADOR DE ESE PAIS, MUESTRA LA MEDIA DEL POTENCIAL QUE HAY EN TODOS SUS JUGADORES
# Y TAMBIEN MUESTRA LA CALIFICACION DEL JUGADOR MEJOR RANKEADO DE CADA PAIS 
print("\n\n\t\t\t EDAD MAS ALTA, MEDIA DEL POTENCIAL Y CALIFICACION MAS ALTA \n\n")   
agrup = df_filtrado.groupby("Nationality").agg({
    "Age" : 'max',
    "Potential" : 'mean',
    "Overall" : 'max'
})
print(agrup)
plt.show(agrup)
#MUESTRA LOS DATOS ANTERIORES DE LOS PRINCIPALES PAISES DEL MUNDO HABLANDO DE FUTBOL

print("\n\n\t\t EDAD MAS ALTA, MEDIA DEL POTENCIAL Y CALIFICACION MAS ALTA PRINCIPALES PAISES \n\n") 
favo = agrup[agrup["Overall"] > 88]
print(favo)
print("\n\n\n\n")

                                                  # 5) VISUALIZACION DE DATOS 
# Comporación entre la pierna preferida de los jugadores en FIFA 2019
sns.countplot(df_filtrado['Preferred Foot'], color = 'blue')
plt.title('PIE PREFRERIDO DE LOS JUGADORES', fontsize = 15)
plt.show()
# Muestra el No. de jugadores por cada posición en FIFA 2019
plt.figure(figsize = (12, 5))
ax = sns.countplot('Position', data =df_filtrado)
ax.set_xlabel(xlabel = 'Diferentes posiciones en el futbol', fontsize = 10)
ax.set_ylabel(ylabel = 'No de jugadores', fontsize = 10)
ax.set_title(label = 'COMPARACION DE JUGADORES Y POSICIONES', fontsize = 15)
plt.show()
# Muestra las 30 nacionalidades con mas jugadores en el FIFA 2019
df_filtrado['Nationality'].value_counts().head(30).plot.bar(figsize = (13, 4))
plt.title('PAISES CON MAS JUGADORES EN FIFA 2019', fontsize = 15)
plt.xlabel('Nombre del pais')
plt.ylabel('Total')
plt.show()
# Comparar el rendimiento de futbolistas zurdos y diestros.
# control de balón vs dribling. 
sns.lmplot(x = 'BallControl', y = 'Dribbling', data = df_filtrado, col = 'Preferred Foot')
plt.show()











