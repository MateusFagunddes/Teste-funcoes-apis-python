from random import randint
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

while True:
    numPensado = randint(1,10)
    contador = 1
    print(f'{Style.BRIGHT}{Fore.LIGHTRED_EX}-=-' * 20)
    tentativa = 0
    while tentativa != numPensado:
        tentativa = int(input('insira um numero 1 à 10: '))
        if tentativa == numPensado:
            print(f'{Fore.GREEN}parabéns vc acertou o numero pensado foi {Fore.MAGENTA}{numPensado}{Fore.GREEN}, e só levou {Fore.MAGENTA}{contador}{Fore.GREEN} tentativas!')
            time.sleep(3)
            break
        else: 
            print(f'{Fore.RED}errooooou, tente denovo.')
        contador += 1