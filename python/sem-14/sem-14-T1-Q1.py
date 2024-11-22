def comprimento(lista):
    contador = 0
    for item in lista:
        contador += 1
    return contador

def inverter(lista):
    lista_invertida = []
    for item in lista:
        lista_invertida.insert(0, item)
    return lista_invertida

def minimo(lista):
    if not lista:
        return None
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item
    return menor

def maximo(lista):
    if not lista:
        return None
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior

def soma(lista):
    total = 0
    for item in lista:
        total += item
    return total

def main():
   
    valores = []
    while True:
        try:
            valor = int(input("Digite os valores (digite 0 para encerrar):"))
            if valor == 0:
                break
            valores.append(valor)
        except ValueError:
            print("Por favor, digite um número válido.")
    
    print(f"Lista lida: {valores}")
    
    print(f"Comprimento da lista: {comprimento(valores)}")
    print(f"Lista invertida: {inverter(valores)}")
    print(f"Menor valor: {minimo(valores)}")
    print(f"Maior valor: {maximo(valores)}")
    print(f"Soma dos valores: {soma(valores)}")

if __name__ == "__main__":
    main()
