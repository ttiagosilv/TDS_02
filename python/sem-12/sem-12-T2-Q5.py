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

def encontrar_primos(x, y):
    primos = []
    for n in range(x, y + 1):
        if e_primo(n):
            primos.append(n)
    return primos

try:
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))

    primos = encontrar_primos(x, y)
    
    if primos:
        for primo in primos:
            print(primo)
    else:
        print("Não há números primos no intervalo especificado.")

except ValueError:
    print("Entrada inválida. Por favor, insira números inteiros.")
