import requests
import json

requisicao = requests.get('http://www.7timer.info/bin/api.pl?lon=-52.00.50&lat=-28.04.05&product=astro&output=json')
previsao = requisicao.json()

print(previsao)