#1.Lê dois números e mostre os seguintes resultados:
#a. Dividendo:
#b. Divisor:
#c. Quociente:
#d. Resto (para calcular o resto de uma divisão, utilize o operador MOD.
num1 = float(input('Informe o primeiro número \n'))
num2 = float(input("Informe o segundo número \n"))
print("----Partes da divisão:----")
print ("A- Dividendo: " , num1)
print("B- Divisor: ", num2)
print("C-Quociente: ", num1 / num2) 
rest = (num1 % num2) 
print("D- Resto :", rest)