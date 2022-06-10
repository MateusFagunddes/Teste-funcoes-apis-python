import requests, json
from time import sleep
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL,CAD-BRL')
cotacao = requisicao.json()
frases = []

def criaFrases(lista: list):
    for i in cotacao:
        coin = cotacao[i]
        lista.append(f'OPERAÇÃO:({coin["name"]}) O 1 {coin["code"]} hoje esta custando: {coin["codein"]} {coin["bid"]} e esta valendo {coin["codein"]} {coin["ask"]}')
    return lista.sort()

def cotacoes():
    print('-'*50)
    code = input('moeda origem: ').upper()
    codein = input('moeda final: ').upper()
    print('-'*50)
    rqs = requests.get(f'https://economia.awesomeapi.com.br/last/{code}-{codein}')
    cot = rqs.json()
    coin = cot[f'{code}{codein}']
    return [f'OPERAÇÃO:({coin["name"]}) O 1 {coin["code"]} hoje esta custando: {coin["codein"]} {coin["bid"]} e esta valendo {coin["codein"]} {coin["ask"]}']

def maiorValor():
    maior = 0
    for i in frases:
        if len(i) > maior:
            maior = len(i)
    return maior

def desenhaDashBoard(lista):
    criaFrases(frases)
    print('┌' + '─' * (maiorValor()+3) + '┐')
    for i,frase in enumerate(lista):
            sleep(0.3)
            print(f"| {frase}", ' ' *(maiorValor() - len(frase)), '│\n', end='')
            if i != (len(lista)-1):
                print('|','─' * (maiorValor()+1), '|')  
    print('└' + '─' * (maiorValor()+3) + '┘')

run = True
while run:
    desenhaDashBoard(frases)
    ask = 's'
    while ask != 'n':
        ask = input('\ndeseja ver mais alguma cotação? [s/n]: ')
        if ask == 's':
            desenhaDashBoard(cotacoes())
    else:
        input('Pressione enter para finalizar.')
        run = False ;
        