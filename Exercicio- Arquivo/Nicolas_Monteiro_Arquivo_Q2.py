'''
2. Faça um programa que permite cadastrar pessoas com os seguintes
dados: nome e idade. Grave esses dados em um arquivo de txt.
O sistema ainda terá opção de cadastrar um nova pessoa e de listar as
pessoas que estão gravadas no arquivo.
Ao cadastrar uma nova pessoa, não deve apagar os registros
anteriores.
'''
esc = 0
while esc != 3:
    print('§'*7, 'CADASTRO', '§'*7)
    print('1- Novo Cadastro')
    print('2- Consultar cadastrados')
    print('3- Sair')
    esc = int(input('Informe sua opção: '))

    if esc == 1:
        sair = ()
        while sair != 's':
            nome = input("Nome: ")
            idade = input('Idade: ')
            with open('cadastropessoas.txt', 'a') as arquivo:
                arquivo.write('Cadastrado')
                arquivo.write('\n')
                arquivo.write('Nome: ')
                arquivo.write(nome)
                arquivo.write('\n')
                arquivo.write('Idade: ')
                arquivo.write(idade)
                arquivo.write('\n')
                arquivo.write('-'*20)
                arquivo.write('\n')

            sair = input('Deseja sair (s/n)?')
            '''
            Forma alternativa de usar o sair, sem o while de cima.
            Poderia usar for também.
            if sair == 's':
                break
            '''
    if esc == 2:
        with open('cadastropessoas.txt', 'r') as arquivo:
            for line in arquivo:
                print(line)
