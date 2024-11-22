def inverter_numero(numero):

    numero_str = str(numero)  
    numero_invertido = numero_str[::-1]
    return numero_invertido

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        numero_invertido = inverter_numero(numero)
        print(f"{numero} {numero_invertido.lstrip('0')}")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()
