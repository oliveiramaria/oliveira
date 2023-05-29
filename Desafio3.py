salario = float(input("Qual o salario do funcionario?: "))
if salario > 8250.00:
    novosalario = salario + salario * 0.1
else:
    novosalario = salario + salario * 0.15  

print("O seu novo salario e " , novosalario)   