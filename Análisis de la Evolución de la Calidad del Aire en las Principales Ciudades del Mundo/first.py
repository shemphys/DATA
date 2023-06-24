import requests
import pandas as pd

# Endpoint de la API
url = 'https://api.openaq.org/v2/measurements'

cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mumbai', 'Cairo', 'Mexico City', 'Beijing', 'Osaka', 'New York']

# Query params
for city in cities:
    params = {
        'city': city,
        'parameter': 'pm25',
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

print(df.head())
df_all.to_json('air_quality_data.json', orient='records', lines=True)

###############NOTES###############
# hay que medir más niveles:
# PM2.5, PM10, CO2, SO2, O3 y NO2
# por ahora solo mido PM2.5
