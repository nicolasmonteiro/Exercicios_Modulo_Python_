'''
4-Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a médias de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente. O programa deve mostrar as informações
como na imagem.
'''
boletim = list()
while True:

    nome = str(input('Informe seu nome: '))
    nota1 = float(input('Informe a nota 1: '))
    nota2 = float(input('Informe a nota 2: '))
    media = (nota1+nota2)/2
    boletim.append([nome, [nota1, nota2], media])
    continua = str(input('Deseja continuar? (s/n)'))
    if continua in 'Nn':
        break
print('-' * 30)
# print(f'{"Nº.":<4}{"Nome":<10}{"Média":>8.1f}')
print('N°', 'Nome', 'Média')
print('-' * 30)
for j, b in enumerate(boletim):
    #print(f'{j:<4}{b[0]:<10} {b[2]:>8.1f}')
    print(j, '', b[0], '', b[2])
while True:
    print('-' * 40)
    esc = int(input("Deseja exibir notas de qual aluno? (555: encerra) "))
    if esc == 555:
        print('Encerrando...')
        break
    if esc <= len(boletim) - 1:
        print("Notas de:", boletim[esc][0], "são:", boletim[esc][1])
print("Obrigado por utilizar o Boletim eletrônico ")
