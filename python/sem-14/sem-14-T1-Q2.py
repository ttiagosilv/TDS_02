def count(lista, valor):
    ocorrencias = 0
    for item in lista:
        if item == valor:
            ocorrencias += 1
    return ocorrencias

def processar_e_exibir_resultados():
    lista = []
    while True:
        try:
            valor = int(input("Digite os valores da lista (digite 0 para encerrar):"))
            if valor == 0:
                break
            lista.append(valor)
        except ValueError:
            print("Por favor, digite um número válido.")

    try:
        valor_pesquisa = int(input("Digite o valor para pesquisar: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        return

    resultado = count(lista, valor_pesquisa)
    print(f"Lista lida: {lista}")
    print(f"Valor pesquisado: {valor_pesquisa}")
    print(f"Número de ocorrências de {valor_pesquisa}: {resultado}")

def main():
    processar_e_exibir_resultados()

if __name__ == "__main__":
    main()
