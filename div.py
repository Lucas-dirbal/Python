num1 = int(input("Digite o 1ºnumero"))
num2 = int(input("Digite o 2ºnumero"))


if num2 == 0 :
    print("divisao por 0 nao é permitida")
else:
    resultadoDiv = num1 / num2
    print(f"A divisão de {num1} por {num2} é {resultadoDiv}")