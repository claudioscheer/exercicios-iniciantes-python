def somar(a, b):
    resultado = a + b
    return resultado


a = input("Digite o primeiro número: ")
a = int(a)
b = input("Digite o segundo número: ")
b = int(b)

resultado = somar(a, b)
print(f"O resultado é: {resultado}")
