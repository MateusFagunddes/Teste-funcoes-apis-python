from webbrowser import get
import requests
import json
from time import sleep

def maiorValor(frases):
    maior = 0
    for frase in frases:
        if len(frase) > maior:
            maior = len(frase)
    return maior

def getJoke():
    baseEN = requests.get('https://v2.jokeapi.dev/joke/Any')
    bdJokesEN = baseEN.json()
    frases = [f"{bdJokesEN['setup']}" , f"{bdJokesEN['delivery']}"]
    return frases

def mostraFrase(frase):
    maior__ = maiorValor(getJoke())     
    print('┌' + '─' * (maior__ -5) + '┐')
    for i in frase:
        print(f'| {i}',' ' * (maior__ -10), "|")

running = True
while running:
    mostraFrase(getJoke())
    close =  input('\nenter for more or "n" for quit.\n>') 

    if close == 'n':
        running = False
else:
    input('...')