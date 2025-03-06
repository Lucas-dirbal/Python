palavraSecreta = "amora".upper()

letrasAcertadas = ["_","_","_","_","_"]
print(letrasAcertadas)

enforcou = False
acertou = False
erros = 0

while(not enforcou and not acertou):
    
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()

    if (chute in palavraSecreta):
        index = 0

        for letra in palavraSecreta:
            if(chute.upper() == letra.upper()):
                letrasAcertadas[index] = letra
            index = index + 1
    print(letrasAcertadas)
print("Fim de Jogo")