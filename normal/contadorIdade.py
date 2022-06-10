for i in range(1, 7+1):
    idade = 2022 - int(input('Insira o ano que você nasceu: '))
    if idade >= 21:
        print(f'sua idade é {idade} anos, por tanto você já é de maior')
    else:
        print(f'sua idade é {idade} anos, por tanto você já é de menor')