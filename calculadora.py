print("Bem vindo(a) !")
print("1 - Adiçao")
print("2 - Subtração")
print("3 - Multipicação")
print("4 - divisão")
oper = int(input("Escolha qual operação voce deseja: "))

if oper == 1:
    num1 = int(input("Digite um número: "))
    num2 = int(input(f"Digite um valor a ser somado a {num1}: "))

    res = num1 + num2

    print(f"A soma de {num1} mais {num2} é igual a {res} !")

elif oper == 2:
    num1 = int(input("Digite o um numero: "))
    num2 = int(input(f"Digite o valor a se subtrair de {num1}: "))

    resSub = num1 - num2

    print(f"A subtração de {num1} menos {num2} é {resSub}")

elif oper == 3:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input(f"Digite o numero a multiplicar {num1}: "))

    resultadoMult = num1 * num2

    print(f"A multiplicaçõa de {num1} vezes {num2} é {resultadoMult}")

elif oper == 4:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input(f"Digite o numero a dividir {num1}: "))
    if num2 == 0 :
         print("divisao por 0 nao é permitida")
    else:
        resultadoDiv = num1 / num2
        print(f"A divisão de {num1} por {num2} é {resultadoDiv}")
else:
    print("Invalido !")