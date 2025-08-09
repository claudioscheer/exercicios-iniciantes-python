soma = 0

i = 0
while i <= 100:
    resto = i % 2
    if resto == 0:
        soma = soma + i
    i = i + 1

print(f"A soma dos números pares entre 0 e 100 é {soma}")
