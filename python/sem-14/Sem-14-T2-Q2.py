def ler_numeros(tamanho):
    numeros = []
    for i in range(tamanho):
        while True:
            try:
                numero = int(input(f"Digite o número {i+1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor, digite um número real válido.")
    return numeros

def calcular_quantidade_negativos(numeros):
    quantidade_negativos = sum(1 for numero in numeros if numero < 0)
    return quantidade_negativos

def calcular_soma_positivos(numeros):
    soma_positivos = sum(numero for numero in numeros if numero > 0)
    return soma_positivos

def main():
    tamanho = 10
    numeros = ler_numeros(tamanho)
    quantidade_negativos = calcular_quantidade_negativos(numeros)
    soma_positivos = calcular_soma_positivos(numeros)

    print("Lista dos números:", numeros)
    print(f"Quantidade de números negativos: {quantidade_negativos}")
    print(f"Soma dos números positivos: {soma_positivos}")

if __name__ == "__main__":
    main()

