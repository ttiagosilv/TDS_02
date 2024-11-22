def soma_cumulativa(lista):

    cumulativa = []
    soma = 0
    for valor in lista:
        soma += valor
        cumulativa.append(soma)
    return cumulativa

def ler_numeros():

    numeros = []
    
    while True:
        try:
            numero = float(input("Digite um número: "))
            if numero == 0:
                break
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número real.")
    
    return numeros

def formatar_lista(lista):
    lista_formatada = []
    for numero in lista:
        if numero.is_integer():
            lista_formatada.append(int(numero))
        else:
            lista_formatada.append(numero)
    return lista_formatada

def main():
    lista_numeros = ler_numeros()
    lista_cumulativa = soma_cumulativa(lista_numeros)
    lista_formatada = formatar_lista(lista_cumulativa)
    
    print("Lista com soma cumulativa:", lista_formatada)

if __name__ == "__main__":
    main()

