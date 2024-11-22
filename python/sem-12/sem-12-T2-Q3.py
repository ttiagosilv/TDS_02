def calcular_harmonica(n):
    H = 0.0
    for i in range(1, n + 1):
        H += 1 / i
    return H

try:
    n = int(input("Digite um número inteiro positivo: "))
    if n <= 0:
        print("O número deve ser um inteiro positivo.")
    else:
        resultado = calcular_harmonica(n)
        print(f"H = {resultado:.4f}")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
