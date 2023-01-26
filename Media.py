import pandas as pd
import time

#Creamos un timestamp cuando iniciamos 
inicio = time.time()
#Leemos el csv de movies y de ratings y los guardamos en dataframes
df_movies = pd.read_csv('Datos/movies.csv')
df_ratings = pd.read_csv('Datos/ratings.csv')
#Hacemos la media de las valoranciones agrupando por id de la pelicula
df_medias = df_ratings.groupby(['movieId']).mean()
#Eliminamos las columnas que no nos interesan 
df_medias = df_medias.drop(['userId','timestamp'],axis=1)
#Unimos los dos dataframes
df_movies_rating = pd.merge(df_movies,df_medias, on='movieId')
#Imprimimos el resultado de la union de los dataframes
print(df_movies_rating)
#guardamos el dataframe en un csv
df_movies_rating.to_csv("movies_rating.csv")
#Creamos un timestamp cuando acabamos
fin = time.time()
#Imprimimos el tiempo de ejecucuión restando al tiempo de fin el tiempo de inicio
print('La ejecución ha durado: '+ str(fin-inicio) +' s')

