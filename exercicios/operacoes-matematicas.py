a = input("Digite o primeiro número: ")
a = float(a)
operacao = input("Digite a operação que você deseja realizar: ")
b = input("Digite o segundo número: ")
b = float(b)

if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    resultado = a / b
else:
    resultado = "Operação inválida"

print(f"O resultado é: {resultado}")
