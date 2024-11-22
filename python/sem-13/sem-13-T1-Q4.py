def separar_pares_e_impares(numeros):
    pares = []
    impares = []
    
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return numeros, pares, impares

def main():
    numeros = []
    
    while len(numeros) < 20:
        try:
            numero = int(input(f"Digite o número {len(numeros) + 1}: "))
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    
    todos, pares, impares = separar_pares_e_impares(numeros)
    
    print("Lista de todos os números:", todos)
    print("Lista de números pares:", pares)
    print("Lista de números ímpares:", impares)

if __name__ == "__main__":
    main()
