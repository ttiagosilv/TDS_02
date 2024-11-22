def ler_jogadores(tamanho):
    jogadores = []
    for i in range(tamanho):
        nome = input("Nome do jogador: ").strip()
        while True:
            try:
                altura = float(input("Altura do jogador (em metros): "))
                break
            except ValueError:
                print("Por favor, digite uma altura válida (número decimal).")
        jogadores.append((nome, altura))
    return jogadores

def jogador_mais_alto(jogadores):
    mais_alto = max(jogadores, key=lambda jogador: jogador[1])
    return mais_alto

def calcular_media_altura(jogadores):
    total_altura = sum(jogador[1] for jogador in jogadores)
    media = total_altura / len(jogadores)
    return media

def jogadores_acima_media(jogadores, media):
    acima_media = [jogador for jogador in jogadores if jogador[1] > media]
    return acima_media

def main():
    tamanho = 12
    jogadores = ler_jogadores(tamanho)
    nome_mais_alto, altura_mais_alto = jogador_mais_alto(jogadores)
    media_altura = calcular_media_altura(jogadores)
    acima_media = jogadores_acima_media(jogadores, media_altura)

    print("JOGADOR MAIS ALTO DO TIME")
    print(f"{nome_mais_alto}")
    print(f"{altura_mais_alto:.2f}")
    print("ALTURA MÉDIA DO TIME")
    print(f"{media_altura:.2f} metros")
    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for nome, altura in acima_media:
        print(f"{nome}\n{altura:.2f}")

if __name__ == "__main__":
    main()
