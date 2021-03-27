# operaciones basicas
import numpy as np
import pandas as pd 


import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import os
data = pd.read_csv("C:/Users/JoseJ/OneDrive/Escritorio/data.csv")
print(data)

data.head()
def country(x):
    return data[data['Nationality'] == x][['Name','Overall','Potential','Position']]


# Muestra los jugadores de nacionalidad Mexicana. 
print (country('Mexico'))

# Muestra los jugadores de nacionalidad Brasileña.
print (country('Brazil'))
def club(x):
    return data[data['Club'] == x][['Name','Jersey Number','Position','Overall','Nationality','Age','Wage',
                                    'Value','Contract Valid Until']]
# Muestra la información relativa de los jugadores del club mexicano Pumas UNAM
print (club('U.N.A.M.'))
print("\n")
print(data.describe())
# Comporación entre la pierna preferida de los jugadores en FIFA 2019

plt.rcParams['figure.figsize'] = (10, 5)
sns.countplot(data['Preferred Foot'], color = 'blue',edgecolor = 'red')
plt.title('Most Preferred Foot of the Players', fontsize = 20)
plt.show()
# Muestra el No. de jugadores por cada posición en FIFA 2019

plt.figure(figsize = (18, 8))
plt.style.use('fivethirtyeight')
ax = sns.countplot('Position', data = data, palette = 'bone')
ax.set_xlabel(xlabel = 'Different Positions in Football', fontsize = 16)
ax.set_ylabel(ylabel = 'Count of Players', fontsize = 16)
ax.set_title(label = 'Comparison of Positions and Players', fontsize = 20)
plt.show()
# Muestra las diferentes nacionalidades en el FIFA 2019

plt.style.use('dark_background')
data['Nationality'].value_counts().head(80).plot.bar(color = 'orange', figsize = (20, 7))
plt.title('Different Nations Participating in FIFA 2019', fontsize = 30, fontweight = 20)
plt.xlabel('Name of The Country')
plt.ylabel('count')
plt.show()
