def multiplica_constante(lista, constante):
    return [x * constante for x in lista]

def ler_numeros():
    numeros = []
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero == 0:
                break
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    return numeros

def ler_constante():
    while True:
        try:
            constante = int(input("Digite o valor da constante: "))
            return constante
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def main():
    numeros = ler_numeros()
    constante = ler_constante()
    lista_multiplicada = multiplica_constante(numeros, constante)
    print("Nova lista após multiplicação:", lista_multiplicada)
    
if __name__ == "__main__":
    main()
