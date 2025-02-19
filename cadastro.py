print("****************************")
print("Bem vindo a Tela de cadastro")
print("****************************")
while True:
    nome = str(input("Qual seu nome ?"))

    nascimento = int(input("Qual seu ano de nascimento ?"))

    nasc = 2025 - nascimento

    if nasc < 18 :
        print("Você não pode continuar !")
        break
    else:
        cod = input("Qual seu cpf ?")

        print(f"Bem vindo {nome}, portador(a) do cpf {cod} , sua idade {nasc} atende os requisitos para o cadastro !")
        print("Você deseja refazer algum dado ?")
        confirmacao = input("n/s")

        if confirmacao == "s":
            print("Refazando campo")
        else:
            print("cadastro realizado com sucesso !")
            break