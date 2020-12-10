'''
5.Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde
esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado. Se der empate, faça outra rodada só com quem deu
empate até sair o vencedor.

'''
import random
import operator
jogadores = dict()
i = 1
valor = 0
empate = True


print('Valores sorteados: ')
for j in range(0, 4):
    jogadores['jogador'+str(j+1)] = random.randint(1, 6)

# modifica o random para ser único
while empate:
    for k, v in jogadores.items():
        dado = random.randint(1, 6)
        if dado not in jogadores.values():
            jogadores[k] = dado
            empate = False
        else:
            dado = random.randint(1, 6)
            empate = True
            # print(jogadores)

# imprime os números dos novos valores do dicionário
for k, v in jogadores.items():
    print(f'O {k} tirou  {v} no dado')
print('')
# ordena descrente
ord_dic = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)
for l in ord_dic:
    print("Ordem dos mais pontuados", l)
print('')

# exibe o ranking
print('Ranking dos jogadores: ')
for j in range(0, len(ord_dic)):
    print(i, 'º lugar:', ord_dic[j][0], 'com ', ord_dic[j][1], 'pontos')
    i += 1
