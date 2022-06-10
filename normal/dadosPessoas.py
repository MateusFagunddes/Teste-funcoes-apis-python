
nome_mais_velho = ''
homem_mais_velho = 0
soma_idade = 0
mulheres_menos_vinte_anos = 0
for i in range(1, 5):
    print('____________________________')
    nome = str(input(f'insira o nome da {i}ª: '))
    idade = int(input(f'insira a idade da {i}ª: '))
    sexo = str(input(f'insira o sexo da {i}ª(f/m): '))
    soma_idade += idade
    if i == 1 and sexo in 'Mm':
        homem_mais_velho = idade
        nome_mais_velho = nome
    elif sexo in 'Mm' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_mais_velho = nome
    if sexo in 'Ff':
        if idade < 20:
            mulheres_menos_vinte_anos += 1



media_idade = soma_idade /4
print('____________________________')
print(f'o homem mais velho tem {homem_mais_velho} anos e se chama {nome_mais_velho}')  
print(f'media das idade é de  {media_idade} anos')  
print(f'{mulheres_menos_vinte_anos} tem menos de 20 anos')  
 
