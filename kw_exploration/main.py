from pytrends.request import TrendReq
import pandas as pd

# Iniciar una sesión de pytrends
pytrends = TrendReq(hl='es-US', tz=360)

# Lista de palabras clave que quieres explorar
kw_list = ["inteligencia artificial", "big data", "blockchain"]

# Obtener los datos de Google Trends para esas palabras clave
pytrends.build_payload(kw_list, timeframe='today 5-y', geo='', gprop='')

# Obtener datos de interés a lo largo del tiempo
data = pytrends.interest_over_time()

# Imprimir los datos
print(data)
