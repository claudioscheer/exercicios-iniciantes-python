from datetime import date


ano_nascimento = input("Digite seu ano de nascimento: ")
ano_nascimento = int(ano_nascimento)

ano_atual = date.today().year

idade = ano_atual - ano_nascimento
print(f"Sua idade é: {idade}")
