'''
1.Usando essa tabela do campeonato pernambucano. Criei uma tupla preenchida com esses times na ordem de colocação depois:
Mostre os 3 primeiros colocados •Os últimos 4 colocados da tabela
Uma lista com os times em ordem alfabética em que posição na tabela está o time de Vitória.
'''
campeonatope = ('Sport', 'Nautico', 'Santa Cruz', 'Salgueiro', 'Central',
                'Afogados', 'Vitoria', 'Petrolina', 'America', 'Flamengo ')
print('G3- Os 3 primeiros colocados')
for c in range(0, 3):
    print(campeonatope.index(campeonatope[c]) + 1, '-', campeonatope[c])
print('x' * 20)
print('Z4- Times na lanterna:')
for c in range(6, 10):
    print(campeonatope.index(campeonatope[c]) + 1, '-', campeonatope[c])
print('x' * 20)
print('Times em ordem alfabetica:')
print(sorted(campeonatope))
print('x' * 20)
print('Posição do time Vitoria:', campeonatope.index('Vitoria')+1, 'º')
