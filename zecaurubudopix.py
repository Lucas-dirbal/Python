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
    faturamento1 = float(input("Qual o faturamento do ano 1? "))
elif op == "2":
    faturamento1 = float(input("Qual o faturamento do ano 1? "))
    faturamento2 = float(input("Qual o faturamento do ano 2? "))
elif op == "3":
    faturamento1 = float(input("Qual o faturamento do ano 1? "))
    faturamento2 = float(input("Qual o faturamento do ano 2? "))
    faturamento3 = float(input("Qual o faturamento do ano 3? "))
elif op == "4":
    faturamento1 = float(input("Qual o faturamento do ano 1? "))
    faturamento2 = float(input("Qual o faturamento do ano 2? "))
    faturamento3 = float(input("Qual o faturamento do ano 3? "))
    faturamento4 = float(input("Qual o faturamento do ano 4? "))
else:
    print("Opção inválida")
    exit()