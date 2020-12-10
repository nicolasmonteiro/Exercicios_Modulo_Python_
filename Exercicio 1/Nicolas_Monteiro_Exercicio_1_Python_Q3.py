#3.Calcular a média final e a situação de um aluno seguindo as seguintes condições: 3 provas
#e obrigação de no mínimo 75% de freqüência . Serão fornecidos pelo usuário as notas das
#três provas e o percentual de freqüência de cada aluno. Com estas informações fornecidas
#apresentar a média final do aluno e a sua situação aprovado ou reprovado. Média para
#aprovação maior ou igual a 7.0.
nota1 = int(input("Informe sua primeira nota: \n"))
nota2 = int(input("Informe sua segunda nota: \n"))
nota3 = int(input("Informe sua terceira nota: \n"))
perc = float(input("Informe a o percentual de frequência:\n"))
media = int((nota1+nota2+nota3)/3)
print("A média do aluno foi:", media)
if (media >= 7) and (perc >=75):
    print("Aluno foi aprovado com média: ", media,"e percentual de :", perc,"%")
else:
    print("Aluno foi reprovado com média: ", media,"e percentual de :", perc,"%")
