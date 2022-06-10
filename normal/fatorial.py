num = int(input('Insira um numero a ser fatorado: '))
contador = num
fator = 1
while contador > 0:
    fator *= contador
    contador -= 1
print(f'{num}! é igual {fator}') 
