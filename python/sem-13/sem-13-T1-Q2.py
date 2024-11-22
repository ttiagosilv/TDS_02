def preencher_com_zeros(n):
    return [0] * n

def preencher_com_numeros(n):

    return list(range(1, n + 1))

def preencher_com_valores(n):
    lista = []
    for i in range(n):
        while True:
            try:
                valor = int(input(f"Digite o valor {i + 1}: "))
                lista.append(valor)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    return lista

def preencher_inversamente_com_valores(n):
    lista = []
    for i in range(n):
        while True:
            try:
                valor = int(input(f"Digite o valor {i + 1}: "))
                lista.insert(0, valor)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    return lista

def obter_numero():
    while True:
        try:
            n = int(input(f"Digite o valor: "))
            if n < 0:
                raise ValueError("O número deve ser zero ou positivo.")
            return n
        except ValueError as e:
            print(e)

def main():
    n = obter_numero()
    if n == 0:
        for _ in range(4):
            print([])
        return
    
    lista_zeros = preencher_com_zeros(n)
    lista_numeros = preencher_com_numeros(n)
    lista_valores = preencher_com_valores(n)
    lista_inversa = preencher_inversamente_com_valores(n)
    
    print(f"\nLista com {n} zeros:", lista_zeros)
    print(f"\nLista com números de 1 a {n}:", lista_numeros)
    print(f"\nLista com {n} valores fornecidos pelo usuário:", lista_valores)
    print(f"\nLista com {n} valores fornecidos pelo usuário na ordem inversa:", lista_inversa)

if __name__ == "__main__":
    main()

