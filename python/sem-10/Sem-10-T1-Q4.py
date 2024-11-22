def gerar_sequencia():
    sequencia = ""
    for i in range(10, 1001, 10):
        sequencia += str(i) + ", "
    sequencia = sequencia[:-2] + "."
    return sequencia

print(gerar_sequencia())