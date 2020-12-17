carros = ['onix', 'ka', 'uno', 'up', 'palio']
combust = [16.7, 15.5, 17, 18.20, 14.2]
consumo = list()
print('Comparativo de Consumo de Combustível')
print('§-'*25)
print('Veículo\t\tNome\t\tKm/l' + '\n')
for i in range(5):
    print("%s\t\t%s\t\t%.2f" %
          (str(i+1), carros[i], combust[i]))
print('§-'*25)
print("\t\tAvaliação Final\n")
for i in range(5):
    litros = 1000/combust[i]
    consumo.append(litros*4.93)
    print(i+1, '-', carros[i], '-', combust[i],
          '- ', "%.2f" % litros, ' litros', ' - R$ ', "%.2f" % consumo[i])
menor = min(consumo)
m_pos = consumo.index(menor)
maior = max(consumo)
ma_pos =consumo.index(maior)
print('O menor consumo é do ', carros[m_pos])
print('O maior consumo é do ', carros[ma_pos])