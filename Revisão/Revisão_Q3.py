soma = 0
m_circ = {'1': [0, 'Precisa da Esfera'], '2': [0, 'Precisa de limpeza'], '3': [
    0, 'Precisa de troca'], '4': [0, 'Quebrado         ']}
print('§-'*20)
print("Digite 0 para encerrar a entrada de dados.")
print('§-'*20)
situacao = input(
    "Informe a cirscunstância do mouse:\n 1- Precisa da Esfera\n 2- Precisa de limpeza\n 3- Precisa de troca\n 4- Quebrado        \n")
soma = 0
while situacao != '0':
    for k, v in m_circ.items():

        if situacao in k:
            m_circ[k][0] = v[0]+1
    situacao = input(
        "Informe a cirscunstância do mouse:\n 1- Precisa da Esfera\n 2- Precisa de limpeza\n 3- Precisa de troca\n 4-Quebrado\n")
for k, v in m_circ.items():
    soma += m_circ[k][0]
print("Quantidade de mouses: ", soma)
print("Cirscunstância\t\t\tQuantidade\t\tPercentual")
for k, v in m_circ.items():
    print(f"{k}-"+str(m_circ[k][1])+"\t\t\t"+str(m_circ[k][0])+"\t\t"
          + str((m_circ[k][0]*100)/soma)+"%")