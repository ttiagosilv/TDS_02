def calcular_media_numeros():
    soma = 0
    contador = 0
    
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo (0 para encerrar): "))
            if numero == 0:
                break
            elif numero > 0:
                soma += numero
                contador += 1
            else:
                print("Digite apenas números inteiros positivos.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    return soma / contador if contador > 0 else None

def main():
    media = calcular_media_numeros()
    if media is not None:
        print(f"A média aritmética dos números digitados é: {media:.2f}")
    else:
        print("Nenhum número válido foi digitado.")

if __name__ == "__main__":
    main()