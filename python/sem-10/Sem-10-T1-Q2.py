def contar_pares_impares():
    quantidade_pares = 0
    quantidade_impares = 0

    for _ in range(100):
        numero = int(input("Digite um número inteiro positivo: "))
        if numero % 2 == 0:
            quantidade_pares += 1
        else:
            quantidade_impares += 1

    print("Quantidade de números pares:", quantidade_pares)
    print("Quantidade de números ímpares:", quantidade_impares)

def main():
    contar_pares_impares()

if __name__ == "__main__":
    main()
