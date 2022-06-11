frase = str(input('digite uma frase(desconsidere acentuação): ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) 
inverso = ''

for i in range(len(junto)-1,-1,-1):
    inverso += junto[i]

if inverso == junto:
    print(f'{junto} de trás para frente se lê {inverso}, por tanto É UM PALINDROMO')
else:
    print(f'{junto} de trás para frente se lê {inverso}, por tanto NÃO É UM PALINDROMO')


