from time import sleep

def contagem_regressiva(num1):
    while num1 > 0:
        num1 = num1 - 1
        print(num1)
        sleep(1)

num1 = int(input("o valor da contagem e"))

contagem_regressiva(num1)