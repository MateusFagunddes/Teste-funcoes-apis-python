import requests, json


rqs = requests.get(f'https://cep.awesomeapi.com.br/json/99001970')
respCep = rqs.json()
#99001970
nomes =  ['cep', 'tipo de endereço', 'nome do endereço', 'endereço', 'estado', 'bairro', 'latitude', 'longitude', 'cidade', 'ibge da cidade', 'DDD']
for i,v in enumerate(respCep):
    print(f'{nomes[i]}: {respCep[v]}')



