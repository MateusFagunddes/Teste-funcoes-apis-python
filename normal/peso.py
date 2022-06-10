maior  = 0 
menor = 0

for i in range(1,5+1):
    peso = float(input(f'insira o peso da {i}ª: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'o maior peso foi de {maior}KG')
print(f'o menor peso foi de {menor}KG')