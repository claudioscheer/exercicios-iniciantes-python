senha = input("Digite a sua senha: ")
caracteres = len(senha)

if caracteres < 8:
    print("Senha inválida.")
else:
    print("Senha válida.")
