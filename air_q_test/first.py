import requests
import pandas as pd
import time

# Endpoint de la API
url = 'https://api.openaq.org/v2/measurements'

cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mumbai', 'Cairo', 'Mexico City', 'Beijing', 'Osaka', 'New York']

# List of pollutants to consider
parameters = ['pm25', 'pm10', 'co2', 'so2', 'o3', 'no2']

# Empty dataframe to storage data
df_all = pd.DataFrame()

# Query params
for city in cities:
    for parameter in parameters:
        params = {
            'city': city,
            'parameter': parameter,
            'date_from': '2013-01-01',
            'date_to': '2023-01-01',
            'limit': 10000,  # how many results you want?? 
            'order_by': 'datetime'
        }

        # API request
        response = requests.get(url, params=params)

        # Converting request into pandas dataframe
        data = response.json()
        #print(data)
        df = pd.DataFrame(data['results'])

        # Add current city to main dataframe
        df_all = pd.concat([df_all, df])

        # 5s pause to avoid API requests per time limits
        time.sleep(5)

print(df.head())
df_all.to_json('air_quality_data.json', orient='records', lines=True)

###############NOTES###############
# hay que medir más niveles:
# PM2.5, PM10, CO2, SO2, O3 y NO2
# por ahora solo mido PM2.5
