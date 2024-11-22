def ordenar_numeros(num1, num2, num3):
    
    lista_numeros = [num1, num2, num3]
    
    lista_numeros.sort()
    
    for numero in lista_numeros:
        print(numero)

def ler_numeros():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    
    return num1, num2, num3

def main():
    num1, num2, num3 = ler_numeros()
    
    ordenar_numeros(num1, num2, num3)

if __name__ == "__main__":
    main()