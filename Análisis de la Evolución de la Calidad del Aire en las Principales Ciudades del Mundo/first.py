import requests
import pandas as pd

# Endpoint de la API
url = 'https://api.openaq.org/v2/measurements'

# Parámetros de la consulta
params = {
    'city': 'London',
    'parameter': 'pm25',
    'date_from': '2013-01-01',
    'date_to': '2023-01-01',
    'limit': 10000,  # depende del número de resultados que desees obtener
    'order_by': 'datetime'
}

# Realizar la petición a la API
response = requests.get(url, params=params)

# Convertir la respuesta en un dataframe de pandas
data = response.json()
#print(data)
df = pd.DataFrame(data['results'])

print(df.head())
df.to_json('air_quality_data.json', orient='records', lines=True)

