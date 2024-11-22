def calcular_imc(massa, altura):
    return massa / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obeso leve"
    elif imc < 40:
        return "Obeso moderado"
    else:
        return "Obeso mórbido"

def main():
    # Solicitar ao usuário que insira a massa (peso) e a altura
    massa = float(input("Digite sua massa em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    # Calcular o IMC
    imc = calcular_imc(massa, altura)

    # Classificar o IMC e exibir a mensagem correspondente
    classificacao = classificar_imc(imc)
    print("Seu IMC é:", imc)
    print("Classificação:", classificacao)

if __name__ == "__main__":
    main()
