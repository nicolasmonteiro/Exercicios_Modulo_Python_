'''
1. Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um
par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11,
você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de
"craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu
"Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''
import random
dado2 = 0
dado1 = random.randint(2, 12)
'''
dado1 = ramdom.randint(1, 6)
dado2 = ramdom.randint(1, 6)
soma1 = dado1 + dado2
#Poderia utilizar dois dados em vez de um, mas percebi uma coisa ao testar, por ser a soma de dois dados poderia repetir o mesmo número com maior
frequência, como por exemplo: 7, pode ser 6 + 1 ou 3 + 4 ou 2 + 5. Então por conta dessa incidência maior coloquei apenas como se fosse um dado com 12 .
Mas poderia substituir facilmente por soma dos dois dados, como de fato seria na prática. 
Uma das vantagens que vi também foi poder conseguir diminuir ainda mais as linhas do código.
'''
jogada = (input('Deseja jogar os dados?(s): '))
if jogada == 's':
    print(dado1)
    if dado1 == 7 or dado1 == 11:
        print('Você é natural, venceu!')
    if dado1 == 2 or dado1 == 3 or dado1 == 12:
        print('Craps, você perdeu')
    if dado1 == 4 or dado1 == 5 or dado1 == 6 or dado1 == 8 or dado1 == 9 or dado1 == 10:
        print('Ponto! Tente acertar de novo esse número para ganhar')
        while dado2 != dado1:
            jogadanova = input('Pronto pra jogar novamente?(s): ')
            jogadanova == 's'
            dado2 = random.randint(2, 12)
            print(dado2)
            if dado2 == 7:
                print('Você perdeu!')
                break
            if dado2 == dado1:
                print('Você venceu!')
                break
