def intercalar_listas(lista_a, lista_b):
    lista_c = []
    for a, b in zip(lista_a, lista_b):
        lista_c.append(a)
        lista_c.append(b)
    return lista_c

def main():
    lista_a = []
    lista_b = []

    while len(lista_a) < 25:
        try:
            numero = int(input(f"Digite o número {len(lista_a) + 1} para a lista A: "))
            lista_a.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    
    while len(lista_b) < 25:
        try:
            numero = int(input(f"Digite o número {len(lista_b) + 1} para a lista B: "))
            lista_b.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    
    lista_c = intercalar_listas(lista_a, lista_b)
    
    print("Lista A:", lista_a)
    print("Lista B:", lista_b)
    print("Lista C (intercalada):", lista_c)

if __name__ == "__main__":
    main()
