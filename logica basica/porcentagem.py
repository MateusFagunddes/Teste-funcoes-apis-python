import time
import colorama
from colorama import Fore, Back , Style
colorama.init(autoreset=True)
continuar = 's'
while continuar == 's':
    print(f'{Fore.LIGHTWHITE_EX}Insira o valor: ')
    valor = float(input('> '))
    print(f'{Fore.LIGHTWHITE_EX}Insira a porcentagem: ')
    x = float(input('> '))
    porc = (x/100)*valor


    print(f'{Fore.GREEN}Digite qual opção dejesa realizar. ')
    print(f'{Fore.GREEN}1. Adição.')
    print(f'{Fore.GREEN}2. Subtração. ')
    solicitacao= int(input('> '))

    if solicitacao == 1 or solicitacao ==2:
        if solicitacao ==1 :
            soma= porc + valor
            print(f'{x:.2f}% de {valor} + {valor} = {Fore.LIGHTBLUE_EX}{soma:.2f}')
        if solicitacao ==2 :
            subtracao= valor - porc
            print(f'{x:.2f}% de {valor} - {valor} = {Fore.LIGHTBLUE_EX}{subtracao:.2f}')
    else:
        print(f'{Fore.RED}Solicitação invalida!')        
    
    #encerar ou continuar a aplicação
    print(f'{Fore.GREEN} deseja continuar?[s,n]')
    continuar = input('> ')
    if continuar == 's' or continuar == 'n':
        if continuar == 'n':
            print(f'{Fore.CYAN}Obrigado por usar nossa aplicação!')
            time.sleep(2)
            break
    else:
        print(f'{Fore.LIGHTRED_EX} solicitação invalida! {Fore.MAGENTA}A aplicação será interrompida!')  
        time.sleep(2)      
