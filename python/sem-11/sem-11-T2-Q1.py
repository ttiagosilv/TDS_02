def main():
    soma = 0 
    while True:
        try:
            numero = int(input("Digite um número inteiro (0 para encerrar): "))   
            if numero == 0:
                break
            soma += numero    
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    print(f"A soma dos números digitados é: {soma}")

if __name__ == "__main__":
    main()
