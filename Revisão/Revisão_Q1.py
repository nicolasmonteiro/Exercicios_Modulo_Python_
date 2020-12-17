faixas = [[200, 299], [300, 399], [400, 499], [500, 599], [600, 699],[700, 799], [800, 899], [900, 999]]
cont = [0]*9
vendas = 0

print("Informe 0 para ver relatório de sálarios dentro do intervalo.")
vendas = float(input('Informe o valor de vendas: '))
    
while vendas != 0:
    sal = (vendas*9)/100+200
    if sal < 1000:
        for i in range(8):
            if sal > faixas[i][0] and sal < faixas[i][1]:
                cont[i] += 1
    else:
        cont[8] += 1
    vendas = float(input("Informe o valor das vendas:"))
print('§-'*20)
for i in range(8):
    print("Entre R$", faixas[i][0], "e R$", faixas[i]
          [1], ":", cont[i], "vendedores.")
print("Salarios acima que R$1000:", cont[8], "vendedores.")
print('§-'*20)
    