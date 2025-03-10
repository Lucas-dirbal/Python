palavraSecreta = "amora".upper()

letrasAcertadas = ["_","_","_","_","_"]
print(letrasAcertadas)

enforcou = False
acertou = False
erros = 1

while not enforcou and not acertou:
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()

    if chute in palavraSecreta:
        index = 0
        for letra in palavraSecreta:
            if chute == letra:
                letrasAcertadas[index] = letra
            index += 1
    else:
        print(f"Você errou, Total de  erros {erros} !")
        erros += 1

    enforcou = erros == 6
    acertou = "_" not in letrasAcertadas
    print(letrasAcertadas)

    if acertou:
        print("Você ganhou!")
    elif enforcou:
        print("Você perdeu!")

print("Fim de Jogo")
