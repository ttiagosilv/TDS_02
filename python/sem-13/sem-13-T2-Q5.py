def esta_ordenado(lista):
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))

def ler_lista(n):
    lista = []
    
    for i in range(n):
        while True:
            try:
                valor = float(input(f"Digite o valor {i + 1}: "))
                lista.append(valor)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número real.")
            except EOFError:
                print("Entrada não disponível. Por favor, insira um número real.")
                return [] 
    return lista

def main():
    while True:
        try:
            n = int(input("Digite a quantidade de elementos da lista: "))
            if n <= 0:
                print("A quantidade deve ser um número inteiro positivo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    
    lista = ler_lista(n)
    if lista:
        if esta_ordenado(lista):
            print("LISTA ORDENADA")
        else:
            print("LISTA NÃO ORDENADA")
    else:
        print("LISTA NÃO DISPONÍVEL")
if __name__ == "__main__":
    main()
