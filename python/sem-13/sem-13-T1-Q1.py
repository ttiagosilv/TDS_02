def calcular_soma(numeros):
    return sum(numeros)

def calcular_produto(numeros):
    produto = 1
    for numero in numeros:
        produto *= numero
    return produto

def processar_numeros(numeros):
    if len(numeros) != 10:
        raise ValueError("A lista deve conter exatamente 10 números inteiros.")
    
    print("Números:", numeros)
    soma = calcular_soma(numeros)
    print("Soma:", soma)
    
    produto = calcular_produto(numeros)
    print("Multiplicação:", produto)

def main():
    numeros = []
    
    while len(numeros) < 10:
        try:
            numero = int(input(f"Digite o número {len(numeros) + 1}: "))
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    
    try:
        processar_numeros(numeros)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

