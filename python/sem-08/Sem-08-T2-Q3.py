def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FIZZBUZZ"
    elif numero % 3 == 0:
        return "FIZZ"
    elif numero % 5 == 0:
        return "BUZZ"
    else:
        return str(numero)

def main():
    numero = int(input("Digite um número inteiro positivo: "))

    resultado = fizz_buzz(numero)
    print(resultado)

if __name__ == "__main__":
    main()
