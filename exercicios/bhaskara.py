import math


a = input("Digite o valor de a: ")
a = float(a)

b = input("Digite o valor de b: ")
b = float(b)

c = input("Digite o valor de c: ")
c = float(c)

delta = (b ** b) - (4 * a * c)

if delta < 0:
    print("Delta menor que 0.")
    exit()
elif a == 0:
    print("a precisa ser diferente de zero.")
    exit()

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"x1 = {x1}, x2 = {x2}")
