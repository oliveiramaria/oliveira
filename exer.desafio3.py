num = int(input("Digite um numero para ver a sua tabuada: "))


for cont in range(1,11):
    resultado = num * cont
    print(num,"x",cont,"=", resultado)
print("fim")