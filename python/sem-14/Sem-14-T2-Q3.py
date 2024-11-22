def ler_numeros(tamanho):

    for i in range(tamanho):
        while True:
            try:
                numero = int(input(f"Digite o número {i+1}: "))
                yield numero
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

def eliminar_repetidos(numeros):
    return list(dict.fromkeys(numeros))

def main():
    tamanho = 20
    numeros = list(ler_numeros(tamanho))
    numeros_sem_repetidos = eliminar_repetidos(numeros)

    print("Lista sem elementos repetidos:", numeros_sem_repetidos)

if __name__ == "__main__":
    main()

