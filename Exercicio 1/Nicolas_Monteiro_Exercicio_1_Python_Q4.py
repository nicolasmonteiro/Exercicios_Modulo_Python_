#4.Jogo da Forca: A palavra é adicionada pelo jogador e verifica se já escreveu uma letra.
print('*********************************')
print('*** Jogo da Forca!***')
print('*********************************')
rep= []
palsecret = str(input("Digite a palavra chave : \n"))
letacert = []
for i in palsecret:
    letacert.append('_')
enforc = False
acert = False
erros = 0
print(letacert)
while(not enforc and not acert):
    tent = input("Qual letra? \n")
    if tent in rep:
        print(' Letra já informada, tente outra letra diferente')
    else:
        rep += tent
    if(tent in palsecret):
        pos = 0
        for let in palsecret:
            if(tent.upper() == let.upper()):
                letacert[pos] = let
            pos = pos + 1
    else:
        erros += 1
    enforc = erros == 6  
    acert = '_' not in letacert
    print(letacert)
if(acert):
    print('You Win!!!')
else:
    print('You Lose!!\n')
print('Game over')