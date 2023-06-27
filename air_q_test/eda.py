import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Las modificaciones se hacen en el buffer, no en la base de datos original.


df = pd.read_json('air_quality_data.json', lines=True)

# primeras filas del DataFrame
print(df.head())

# mostrar info básica del DataFrame
print(df.info())

'''
1. Valores no nulos: 'city' y 'isAnalysis' tienen todos sus valores como nulos. borramos variables.
2. Tipo de datos: 'date' es tipo object, habrá que pasarlo a 'datetime'
3. Columnas innecesarias: 'isMobile' = False (en todo, así que eliminar). 'location_id' no es más que un identificador, así que borrar
'''

# Elimina las columnas innecesarias
df = df.drop(['locationId', 'city', 'isAnalysis', 'isMobile'], axis=1)

# Convierte la columna 'date' a datetime
# Extraer la fecha y hora 'utc' de la columna 'date'
df['date'] = df['date'].apply(lambda x: x['utc'])
# Convertir la columna 'date' a datetime
df['date'] = pd.to_datetime(df['date'])


print(df.info())


df.describe(include='all')

#BOXPLOT
# Asumiendo que 'df' es tu DataFrame y 'value' es la columna que quieres analizar
sns.boxplot(x=df['value'])
plt.show()

#Z-SCORES
# Calcula los z-scores
df['value_zscore'] = zscore(df['value'])

# Encuentra los valores atípicos
outliers = df[abs(df['value_zscore']) > 3]



# Cómo mostrar un gráfico
'''
# Suponiendo que "city_name" es el nombre de tu ciudad y "parameter" es tu parámetro de interés (como pm25, pm10, etc.)
city_name = "New Delhi" 
parameter = "pm25"

# Filtramos el dataframe para la ciudad y el parámetro de interés
city_data = df[(df['location'].str.contains(city_name)) & (df['parameter'] == parameter)]

plt.figure(figsize=(15, 8))

# Crear un gráfico de línea del valor de contaminación a lo largo del tiempo
sns.lineplot(x='date', y='value', data=city_data)

plt.title(f'Niveles de {parameter} en el tiempo en {city_name}')
plt.xlabel('Fecha')
plt.ylabel(f'Valor de {parameter}')

plt.show()
'''