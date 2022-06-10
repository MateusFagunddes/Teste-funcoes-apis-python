lista = []
maior = 0
menor = 10**100
posicao_maior = []
posicao_menor = []
for i in range(5):
    lista.append(int(input(f'lendo o {i+1} valor, na posição {i}: ')))
    print('~'*20)

for p, i in enumerate(lista):
    if i >= maior:
        if maior != i:
            posicao_maior.clear()
            posicao_maior.append(p)
        if maior == i:    
            posicao_maior.append(p)
        maior = i
    if i <= menor:
        menor = i
        posicao_menor.append(p)

if len(posicao_maior)> 1:
    frase_maior = 'suas posições são'
else:
    frase_maior = 'sua posição é'

if len(posicao_menor)> 1:
    frase_menor = 'suas posições são'
else:
    frase_menor = 'sua posição é'

print('~'*20)
print(f'o menor numero é {menor} e {frase_menor} {posicao_menor}\n')
print(f'o maior numero é {maior} e {frase_maior} {posicao_maior}')            
