from webbrowser import get
import requests
import json
from time import sleep


def getJoke():
    baseEN = requests.get('https://v2.jokeapi.dev/joke/Any')
    bdJokesEN = baseEN.json()
    frases = [f"| {bdJokesEN['setup']}" , f"| {bdJokesEN['delivery']}"]
    return frases

def mostraFrase(frase):
    def maiorLen(frase):
        maior = 0
        for frase in frase:
            if len(frase) > maior:
                maior = len(frase)   
        return maior
    print('┌'+  '─' * (maiorLen(frase) )+ '┐')
    for i in frase:
        print(f'{i}'+ " "*((maiorLen(frase) - len(i))+1)+ "|")
    print('└' + '─' * (maiorLen(frase)) + '┘')


running = True
while running:
    mostraFrase(getJoke())
    close =  input('\nenter for more or "n" for quit.\n>') 

    if close == 'n':
        running = False
else:
    input('...')