numero = input("Digite o número para gerar a tabuada: ")
numero = int(numero)

limite = input("Informe o limite de números: ")
limite = int(limite)

i = 0
while i <= limite:
    resultado = numero * i
    print(f"{numero}x{i} = {resultado}")
    i = i + 1
