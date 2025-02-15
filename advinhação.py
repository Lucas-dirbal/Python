print("*********************************")
print("Bem-vindo ao jogo de advinhação !")
print("*********************************")

num = 42
tot = 5
rodada = 1

while(rodada <= tot):
    print(f"Tentativa numero {rodada} de {tot} !")

    chute_str = input("De seu palpite !")
    print(f"Você digitou o numero {chute_str}")
    chute = int(chute_str)

    acertou = chute == num
    maior = chute > num
    menor = chute < num

    if(acertou):
        print("Parebens você ganhou um pé de jaca ")
    else:
        if(maior):
            print("O seu palpite é maior !")
        elif(menor):
            print("O seu palpite é menor !")
    rodada = rodada + 1
print("Fim de Jogo !")