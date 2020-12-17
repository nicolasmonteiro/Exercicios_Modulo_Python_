temp = []
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
              'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
for i in range(12):
    temp.append(
        float(input("Informe a temperatura do mês "+str(i+1)+" : ")))

med = sum(temp)/len(temp)
print("-="*20)
print("A média anual das temperaturas: ", "%.2f" % med, "ºC")
print("-="*20)
for j in range(12):
    if temp[j] > med:
        print("Temperatura acima da média ",
              temp[j], "ºC", mes[j])
    elif temp[j] < med:
         print("Temperatura abaixo da média ",
              temp[j], "ºC", mes[j])   