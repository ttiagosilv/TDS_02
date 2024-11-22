def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if nota3 > 8:
        media += 1
    if media > 10:
        media = 10
    return media

def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = calcular_media(nota1, nota2, nota3)
    print("A média das três notas é:", media)

if __name__ == "__main__":
    main()
