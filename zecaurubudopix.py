# 1 - Perguntar o investimento inicial
# 2 - Perguntar a taxa de desconto
# 3 - Perguntar o faturamento do ano 1, 2, 3 e 4
# 4 - Calcular o VPL de cada ano segundo a fórmula
# 5 - faturamento1 / (1 + taxa) ^ tempo
# 6 - somar os VPLs e dimunir o investimento inicial

invsInicial = float(input("Qual o investimento inicial? "))
taxa = float(input("Qual a taxa de desconto ? "))
op = input("Quantos faturamento você quer calcular? (1, 2, 3 ou 4) ")
if op == "1":
    op = 1
    faturamento1 = float(input("Qual o faturamento do ano 1? "))
elif op == "2":
    op = 2
    faturamento1 = float(input("Qual o faturamento do ano 1? "))
    faturamento2 = float(input("Qual o faturamento do ano 2? "))
elif op == "3":
    op = 3
    faturamento1 = float(input("Qual o faturamento do ano 1? "))
    faturamento2 = float(input("Qual o faturamento do ano 2? "))
    faturamento3 = float(input("Qual o faturamento do ano 3? "))
elif op == "4":
    op = 4
    faturamento1 = float(input("Qual o faturamento do ano 1? "))
    faturamento2 = float(input("Qual o faturamento do ano 2? "))
    faturamento3 = float(input("Qual o faturamento do ano 3? "))
    faturamento4 = float(input("Qual o faturamento do ano 4? "))
else:
    print("Opção inválida")
    exit()

# tempo elevado por anos 
if op == 1:
    VPL1 = faturamento1 / (1 + taxa) ** 1
    VPL = VPL1 - invsInicial


elif op == 2:
    VPL1 = faturamento1 / (1 + taxa) ** 1
    VPL = VPL1 - invsInicial
    VLP2 = faturamento2 / (1 + taxa) ** 2
    VPL = VPL1 + VLP2 - invsInicial

elif op == 3:
    VPL1 = faturamento1 / (1 + taxa) ** 1
    VPL = VPL1 - invsInicial
    VLP2 = faturamento2 / (1 + taxa) ** 2
    VPL = VPL1 + VLP2 - invsInicial
    VLP3 = faturamento3 / (1 + taxa) ** 3
    VPL = VPL1 + VLP2 + VLP3 - invsInicial
elif op == 4:
    VPL1 = faturamento1 / (1 + taxa) ** 1
    VPL = VPL1 - invsInicial
    VLP2 = faturamento2 / (1 + taxa) ** 2
    VPL = VPL1 + VLP2 - invsInicial
    VLP3 = faturamento3 / (1 + taxa) ** 3
    VPL = VPL1 + VLP2 + VLP3 - invsInicial
    VLP4 = faturamento4 / (1 + taxa) ** 4
    VPL = VPL1 + VLP2 + VLP3 + VLP4 - invsInicial
else:
    print("Opção inválida")
    exit()
# Exibir o resultado
print("O VPL é: ", VPL)

if VPL > 0:
    print("O seu investimeto gerará lucro")
else:
    print("O seu investimento não gerará lucro")