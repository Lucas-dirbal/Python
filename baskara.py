import math
a = float(input("Qual o valor de A ?\n"))
b = float(input("Qual o valor de B ?\n"))
c = float(input("Qual o valor de C ?\n"))
delta = (b ** 2 ) - (4 * a * c)
if (delta < 0) ;
    print("Delta menor que 0")
else:
    x1 = (-b + math.sqrt(delta)) / (a*2)
    x2 = (-b - math.sqrt(delta)) / (a*2)
    print(f"O x1 é {x1} e o x2 é {x2}")