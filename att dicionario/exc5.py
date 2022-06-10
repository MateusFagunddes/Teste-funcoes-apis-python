pessoas = {}
pessoas_mais_velhas = mulheres = []
soma_idades = contador = 0
continuar = 's'
while True:
    if continuar != 'n':
        contador+=1
        pessoas['nome'] = input("nome: ").capitalize()
        pessoas['idade'] = int(input('idade: '))
        pessoas['genero'] = input('genero(M/F): ').lower()
        soma_idades += pessoas['idade'] 
        continuar = input('deseja continuar? ')
    else: 
        break    
media_idade = soma_idades / contador
for pessoa in pessoas.items():
    if pessoas['idade']> media_idade:
        pessoas_mais_velhas.append(pessoas['nome'])
    if pessoas['genero'] == 'f':
        mulheres.append(pessoas['nome'])  

print('-='*20)
print(f'foram lidas {contador} pesssoas')
print(f'a média de idade foi de {media_idade}')
print(f'as mulheres cadastradas foram: {mulheres}')
print(f'as pessoas com idade acima da média são: {pessoas_mais_velhas}')