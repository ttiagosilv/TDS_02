def tempo_para_alcancar_simulado(distancia_inicial):
    velocidade_tartaruga = 1 
    velocidade_lebre = 10 
    tempo = 0
    distancia_tartaruga = distancia_inicial
    distancia_lebre = 0

    while distancia_lebre < distancia_tartaruga:
        distancia_tartaruga += velocidade_tartaruga
        distancia_lebre += velocidade_lebre
        tempo += 1
    return tempo

distancia_inicial = float(input("Quantos metros a tartaruga sai à frente da lebre? "))
tempo = tempo_para_alcancar_simulado(distancia_inicial)
print(f"A lebre alcançará a tartaruga em {tempo} minutos.")