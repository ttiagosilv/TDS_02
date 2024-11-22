def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        while True:
            try:
                numero = int(input(f"Digite o número {i+1}: "))
                lista.append(numero)
                break
            except ValueError:
                print("Por favor, digite um número real válido.")
    return lista

def calcular_produto_escalar(lista1, lista2):
    termos = [f"({x} x {y})" for x, y in zip(lista1, lista2)]
    produto_escalar = sum(x * y for x, y in zip(lista1, lista2))
    expressao = " + ".join(termos) + f" = {produto_escalar}"
    return produto_escalar, expressao

def main():
    tamanho = 5
    lista1 = ler_lista(tamanho)
    lista2 = ler_lista(tamanho)
    produto_escalar, expressao = calcular_produto_escalar(lista1, lista2)

    print("Conjunto X:", lista1)
    print("Conjunto Y:", lista2)
    print(f"O produto escalar é: {expressao}")

if __name__ == "__main__":
    main()

