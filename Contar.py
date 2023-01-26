import pandas as pd
import time

#Creamos un timestamp cuando iniciamos 
inicio = time.time()
#Leemos el csv de ratings y lo guardamos en un dataframe
df_ratings = pd.read_csv('Datos/ratings.csv')
#Contamos los valores que hay en la columna rating
frecuencia = df_ratings['rating'].value_counts()
#Ordenamos las valoraciones
frecuencia=frecuencia.sort_index(ascending=False)
#Imprimimos el resultado
print(frecuencia)
#Creamos un timestamp cuando acabamos
fin = time.time()
#Imprimimos el tiempo de ejecucuión restando al tiempo de fin el tiempo de inicio
print('La ejecución ha durado: '+ str(fin-inicio) +' s')



