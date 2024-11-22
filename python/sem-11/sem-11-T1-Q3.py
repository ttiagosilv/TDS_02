def encontrar_maior_menor():
    maior = None
    menor = None
    
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo (0 para encerrar): "))
            if numero == 0:
                break 
            if numero > 0:
                if maior is None or numero > maior:
                    maior = numero
                if menor is None or numero < menor:
                    menor = numero
            else:
                print("Por favor, digite apenas números inteiros positivos.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    return maior, menor

def main():
    maior, menor = encontrar_maior_menor()
    if maior is not None and menor is not None:
        print(f"O maior número digitado é: {maior}")
        print(f"O menor número digitado é: {menor}")
    else:
        print("Nenhum número válido foi digitado.")

if __name__ == "__main__":
    main()
