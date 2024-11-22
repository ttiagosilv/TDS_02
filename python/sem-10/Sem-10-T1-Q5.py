def encontrar_maior_numero():
    maior_numero = None

    for i in range(100):
        numero = int(input("Digite um número inteiro positivo: "))
        if maior_numero is None or numero > maior_numero:
            maior_numero = numero

    return maior_numero

print("O maior número é:", encontrar_maior_numero())
