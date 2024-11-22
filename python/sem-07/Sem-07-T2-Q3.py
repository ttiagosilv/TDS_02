def classificar_digitos_impares(numero):
    digito_dezena = numero // 10
    digito_unidade = numero % 10

    if digito_dezena % 2 == 0 and digito_unidade % 2 == 0:
        return "Nenhum dígito é ímpar."
    elif digito_dezena % 2 != 0 and digito_unidade % 2 == 0:
        return "Apenas um dígito é ímpar."
    elif digito_dezena % 2 == 0 and digito_unidade % 2 != 0:
        return "Apenas um dígito é ímpar."
    else:
        return "Os dois dígitos são ímpares."

def main():
    numero = int(input("Digite um número inteiro entre 10 e 99: "))
    if 10 <= numero <= 99:
        mensagem = classificar_digitos_impares(numero)
        print(mensagem)
    else:
        print("Número fora do intervalo.")

if __name__ == "__main__":
    main()