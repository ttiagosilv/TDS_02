def calcular_fatorial(n):
    if n == 0:
        return 1
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

try:
    numero = int(input("Digite um número inteiro não-negativo: "))
    if numero < 0:
        print("O número deve ser não-negativo.")
    else:
        resultado = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é {resultado}.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")

