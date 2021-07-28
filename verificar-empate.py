def verificar_empate(gols_time_a, gols_time_b):
    if gols_time_a == gols_time_b:
        return "empate"
    else:
        return "alguém ganhou"


placar = input("Digite o placar do jogo: ")
gols = placar.split("x")
gols_time_a = gols[0]
gols_time_b = gols[1]

jogo_empatou = verificar_empate(gols_time_a, gols_time_b)
print(f"O resultado do jogo é: {jogo_empatou}")
