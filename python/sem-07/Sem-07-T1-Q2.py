def e_impar(numero):
    return numero % 2 != 0

def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = e_impar(numero)
    print(resultado)

if __name__ == "__main__":
    main()  