def aplicar_multiplicacao(lista):
    nova_lista = []
    for i, valor in enumerate(lista):
        if i % 2 == 0: 
            nova_lista.append(valor * 3)
        else: 
            nova_lista.append(valor * 5)
    return nova_lista

def main():
    numeros = []
    
    while len(numeros) < 100:
        try:
            numero = int(input(f"Digite o número {len(numeros) + 1}: "))
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    
    numeros_ordenados = sorted(numeros)
    
    lista_multiplicada = aplicar_multiplicacao(numeros_ordenados)
    
    print("Nova lista após multiplicação:", lista_multiplicada)

if __name__ == "__main__":
    main()
