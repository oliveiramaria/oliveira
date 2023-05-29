salario = float(input("Qual é o salario do funcionario? R$ " ))
novo = salario + (salario * 12/100)

print("Um funcionario que ganhava R${:.2f}, com 12% de aumento, passa a receber R${:.2f}".format(salario,novo))
