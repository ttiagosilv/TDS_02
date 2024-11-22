def ler_numeros(tamanho):
    numeros = []
    for i in range(tamanho):
        while True:
            try:
                numero = int(input(f"Digite o número {i+1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
    return numeros

def encontrar_maior_e_posicao(numeros):

    maior = max(numeros)
    posicao = numeros.index(maior)
    return maior, posicao

def main():
    tamanho = 10
    numeros = ler_numeros(tamanho)
    maior, posicao = encontrar_maior_e_posicao(numeros)
    
    print(numeros)
    print(f" O maior número é:{maior}")
    print(f"e está na posição:{posicao}")

if __name__ == "__main__":
    main()
