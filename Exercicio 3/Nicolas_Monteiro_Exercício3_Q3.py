'''
3. Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 60 para cada jogo,
cadastrando tudo em uma lista composta.
Exemplo:
Quantos
jogos você quer sortear? 2
Jogo1: 1:1:[4,8,10,20,28,12] Jogo 2: [14, 20, 43, 35, 38,47]
Obs: o número não pode se repetir no mesmo jogo. Mas, não tem problema se repetir em outro jogo
'''
import random
cont = 0
sorteioquant = int(input("Quantos jogos deseja sortear? "))
print('------Palpites Mega Sena--------')
for c in range(0, sorteioquant):
    # while cont != sorteioquant:
    cont += 1
    listaaleatoria = random.sample(range(1, 60), 6)
    print('Jogo', cont, ':', (listaaleatoria))
