def calcular_peso_ideal(altura, sexo):
    if sexo == 1:
        peso_ideal = 72.7 * altura - 58
    elif sexo == 2:
        peso_ideal = 62.1 * altura - 44.7
    else:
        peso_ideal = None
    return peso_ideal

def main():
    altura = float(input("Digite a altura (em metros): "))
    sexo = int(input("Digite o sexo (1 para homens, 2 para mulheres): "))

    peso_ideal = calcular_peso_ideal(altura, sexo)

    if peso_ideal is not None:
        print("O peso ideal é: {:.2f} kg".format(peso_ideal))
    else:
        print("Sexo não reconhecido. Por favor, insira 1 para homens ou 2 para mulheres.")

if __name__ == "__main__":
    main()
