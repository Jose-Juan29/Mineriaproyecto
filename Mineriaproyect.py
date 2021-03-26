import numpy as np 
import pandas as pd 
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS , ImageColorGenerators
import re
from PIL import Image
url="c:/Users/JoseJ/OneDrive/Escritorio/DisneylandReviews.csv"
df=pd.read_csv(url)
print(df)
df=df.loc[df['Year_Month']=='missing']
print(df)
url="c:/Users/JoseJ/OneDrive/Escritorio/DisneylandReviews.csv"
df=pd.read_csv(url,encoding="cp1252",na_values=['missing'])
#== 
df=df.dropna().reset_index()
print ("\nMissing values :  ", df.isnull().sum().values.sum())
print ("Rows     : " ,df.shape[0])
print ("Columns  : " ,df.shape[1])
print ("\nFeatures : \n" ,df.columns.tolist())
print ("\nMissing values :  ", df.isnull().sum().values.sum())
print ("\nUnique values :  \n",df.nunique())
df['Branch'].value_counts()
sns.set_style("whitegrid")
#== 
df3=df.groupby('year',as_index=False).agg({'review length':'sum'})
plt.figure(figsize=(14,7))
plt.plot(df3['year'] ,df3['review length'],marker='o',label='review length by year',color='black')
plt.figure(figsize=(10,6))
sns.countplot(data=df,x='year',hue='Branch',palette='Blues')
plt.figure(figsize=(10,6))
fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=False)
sns.countplot(ax=axes[0],data=df,x='quarter',hue='Rating',palette='gnuplot')
axes[0].set_title('Quarter By Ratings')
sns.countplot(ax=axes[1],data=df,x='quarter',palette='gist_heat')
axes[1].set_title('Quarter per reviews')
#==
