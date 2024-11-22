def e_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    numero = int(input("Digite um número inteiro: "))
    print(e_primo(numero))
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
