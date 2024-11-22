def ler_reais_invertidos(n):
    if n == 0:
        print("[]")
        return
    
    reais = []
    for i in range(n):
        while True:
            try:
                valor = float(input())
                reais.append(round(valor, 4))
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número real.")
    
    reais_invertidos = reais[::-1]
    print(reais_invertidos)

def calcular_media_notas(n):
    if n == 0:
        print("SEM NOTAS")
        print("0")
        return
    
    notas = []
    for i in range(n):
        while True:
            try:
                nota = float(input())
                notas.append(round(nota, 1)) 
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número real.")
    
    media = round(sum(notas) / n, 1)
    print(notas)
    print( media)

def contar_vogais_e_consoantes(n):
    if n == 0:
        print("[]")
        return
    
    vogais = "aeiouAEIOU"
    letras = []
    consoantes = []
    
    for i in range(n):
        while True:
            letra = input().strip()
            if len(letra) == 1 and letra.isalpha():
                letras.append(letra)
                if letra in vogais:
                    continue
                else:
                    consoantes.append(letra)
                break
            else:
                print("Entrada inválida. Por favor, insira uma única letra.")
    
    numero_vogais = len(letras) - len(consoantes)
    print(numero_vogais)
    print(consoantes)

def main():
    while True:
        try:
            n = int(input())
            if n < 0:
                raise ValueError("O número deve ser zero ou positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, insira um número inteiro positivo.")
    
    if n == 0:
        print("[]")
        print("[]")
        print("SEM NOTAS")
        print("0")
        print("[]")
        return
    
    ler_reais_invertidos(n)
    calcular_media_notas(n)
    contar_vogais_e_consoantes(n)

if __name__ == "__main__":
    main()

