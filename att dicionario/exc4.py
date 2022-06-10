aproveitamento = {}
soma_gols= 0
aproveitamento['nome'] = input('Nome do jogador: ').capitalize()
partidas = int(input('Partidas jogadas: '))
aproveitamento['partidas jogadas'] = partidas
aproveitamento['gols'] = list()
for i in range(partidas):
    aproveitamento['gols'].append(int(input(f'Quantidades de gols marcados na {i+1}ᵒ: ')))
    soma_gols += aproveitamento['gols'][i]
aproveitamento['total de gols'] = soma_gols

print('-='*20)
print(f'O jogador: {aproveitamento["nome"]}')
print( f"Jogou {aproveitamento['partidas jogadas']} partidas")

for i , gols in enumerate(aproveitamento['gols']):
    print(f'{" "*5}Na {i+1}ᵒ partida ele marcou {gols}')
print(f'Teve um aproveitamento total de {aproveitamento["total de gols"]} gols')
