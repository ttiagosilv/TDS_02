def calcular_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

def main():
    numeros = []

    for i in range(100):
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)

    media = calcular_media(numeros)
    print("O valor médio dos números é: {:.2f}".format(media))

if __name__ == "__main__":
    main()
