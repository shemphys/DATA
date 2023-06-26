import requests
import pandas as pd
import time

# Endpoint de la API
url = 'https://api.openaq.org/v2/measurements'

# Lista de las 10 ciudades más pobladas del mundo
cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mumbai', 'Cairo', 'Mexico City', 'Beijing', 'Osaka', 'New York']

# Lista de contaminantes a considerar
parameters = ['pm25', 'pm10', 'co2', 'so2', 'o3', 'no2']

# Crear un DataFrame vacío para almacenar todos los datos
df_all = pd.DataFrame()

# Número máximo de intentos para cada solicitud
max_attempts = 3

# Iterar sobre todas las ciudades y contaminantes
for city in cities:
    for parameter in parameters:
        for attempt in range(max_attempts):
            try:
                # Parámetros de la consulta
                params = {
                    'city': city,
                    'parameter': parameter,
                    'date_from': '2013-01-01',
                    'date_to': '2023-01-01',
                    'limit': 5000,  # reducir el límite para solicitudes más manejables
                    'order_by': 'datetime'
                }

                # Realizar la petición a la API
                response = requests.get(url, params=params, timeout=10)  # agregar un límite de tiempo a la solicitud

                # Convertir la respuesta en un dataframe de pandas
                data = response.json()

                if 'results' in data:
                    df = pd.DataFrame(data['results'])
                    # Añadir los datos de esta ciudad y contaminante al DataFrame principal
                    df_all = pd.concat([df_all, df])
                else:
                    print(f"No se encontraron resultados para la ciudad {city} y el parámetro {parameter}. Respuesta completa: {data}")

                # Si la solicitud fue exitosa, salir del bucle de intentos
                break
            except requests.exceptions.RequestException as e:
                print(f"Error en la solicitud para la ciudad {city} y el parámetro {parameter}: {e}")
                if attempt < max_attempts - 1:  # i.e., si no es el último intento
                    print("Intentando nuevamente...")
                    time.sleep(10)  # Esperar un poco antes de intentar nuevamente
                else:
                    print("Se agotaron todos los intentos. Pasando al siguiente parámetro o ciudad.")
            except Exception as e:
                print(f"Otro error ocurrió: {e}")

        # Pausa de 5 segundos entre solicitudes para evitar exceder el límite de la API
        time.sleep(5)

# Guardar el DataFrame en un archivo .json
df_all.to_json('air_quality_data.json', orient='records', lines=True)
