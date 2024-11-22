def encontrar_maior_menor(numeros):
    maior = numeros[0]
    menor = numeros[0]

    for num in numeros:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    return maior, menor

def main():
    print("Digite 5 números inteiros diferentes:")
    numeros = []

    for i in range(5):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

    maior, menor = encontrar_maior_menor(numeros)

    print("O maior número é:", maior)
    print("O menor número é:", menor)

if __name__ == "__main__":
    main()
