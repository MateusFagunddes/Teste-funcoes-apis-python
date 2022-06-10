import colorama
from colorama import Fore
colorama.init(autoreset=True)

while True:
    print(f'{Fore.GREEN}x-'*30)
    num1 = float(input('digite um numero: '))
    num2 = float(input('digite outro numero numero: '))

    print(f'{Fore.CYAN}Escolha uma das opções abaixo:')
    print(f'{Fore.CYAN}1.somar')
    print(f'{Fore.CYAN}2.multiplicar')
    print(f'{Fore.CYAN}3.maior')
    print(f'{Fore.CYAN}4.gerar novos numeros')
    print(f'{Fore.CYAN}5.sair do programa')
    escolha = int(input('> '))
    
    if escolha == 1:
        adicao = num1 + num2
        print(f'{Fore.LIGHTYELLOW_EX}{num1} + {num2} = {adicao}')
    if escolha == 2:
        multiplicacao = num1 * num2    
        print(f'{Fore.LIGHTYELLOW_EX}{num1} * {num2} = {multiplicacao}')
    if escolha == 3:
        if num1> num2:
            print(f'{Fore.LIGHTYELLOW_EX}o maior numero informado foi {num1}')
        else:
            print(f'{Fore.LIGHTYELLOW_EX}o maior numero informado foi {num2}')
    if escolha == 5:
        break

