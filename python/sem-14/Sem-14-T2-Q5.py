def ler_lista(tamanho):
    for i in range(tamanho):
        while True:
            try:
                numero = int(input(f"Digite o número {i+1}: "))
                yield numero
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

def unir_listas(lista1, lista2):
    return list(dict.fromkeys(lista1 + lista2))

def main():
    tamanho = 10
    lista1 = list(ler_lista(tamanho))
    lista2 = list(ler_lista(tamanho))
    lista_uniao = unir_listas(lista1, lista2)

    print("Lista união (sem elementos repetidos):", lista_uniao)

if __name__ == "__main__":
    main()
