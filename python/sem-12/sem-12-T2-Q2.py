def gerar_fibonacci(n):
    fibonacci = [0, 1]

    while len(fibonacci) < n:
        proximo_termo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_termo)

    return fibonacci

try:
    n = int(input("Digite um número inteiro maior ou igual a 2: "))
    if n < 2:
        print("O número deve ser maior ou igual a 2.")
    else:
        fibonacci = gerar_fibonacci(n)
        # Imprime os resultados separados por vírgula
        print(", ".join(map(str, fibonacci)))
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
