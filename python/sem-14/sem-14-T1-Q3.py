def gerar_lista_soma(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

def ler_lista(tamanho):
    lista = []
    while len(lista) < tamanho:
        try:
            valor = int(input())
            lista.append(valor)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    return lista

def main():

    tamanho = 20

    a = ler_lista(tamanho)
    b = ler_lista(tamanho)
    c = gerar_lista_soma(a, b)

    print(f"{a}")
    print(f"{b}")
    print(f"{c}")

if __name__ == "__main__":
    main()
