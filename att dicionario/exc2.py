from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
contador = 0
print('\nnumeros sorteados:\n')
for k,v in jogadores.items():
    print(f'{k} sorteou {v}')
    sleep(0.3)

print('\nRanking dos jogadores:\n')
for k,v in sorted(jogadores.items(), key= itemgetter(1), reverse=True):
    contador +=1
    print(f'{contador}ᵒ lugar: {k} sorteou {v}')
    sleep(0.3)
