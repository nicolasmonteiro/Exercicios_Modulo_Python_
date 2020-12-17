import random


def misturar(vocabulo):
    novo_vocabulo = ""
    novo_vocabulo = random.sample(
        vocabulo.upper(), len(vocabulo)) 
    print('O vocabulo que você informou invertida fica com join: ',
          ''.join(novo_vocabulo))
    print('O vocabulo que você informou embaralhada fica: ', novo_vocabulo)


misturar("salocin")
