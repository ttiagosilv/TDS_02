def somar_condicional(numero):
    if numero % 2 == 0:
        return numero + 5
    else:
        return numero + 8

def main():
    # Solicitar ao usuário que insira um número inteiro
    numero = int(input("Digite um número inteiro: "))

    # Chamar a função somar_condicional para calcular o resultado
    resultado = somar_condicional(numero)

    # Exibir o resultado da operação
    print("O resultado da operação é:", resultado)

if __name__ == "__main__":
    main()
