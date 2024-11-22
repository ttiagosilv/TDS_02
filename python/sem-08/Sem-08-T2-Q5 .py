def calcular_conceito(media_final):
    if media_final >= 9.0:
        return "A"
    elif media_final >= 7.5:
        return "B"
    elif media_final >= 6.0:
        return "C"
    elif media_final >= 4.0:
        return "D"
    else:
        return "E"

def main():
    matricula = input()
    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))
    nota3 = float(input("Digite a nota da terceira prova: "))
    media_exercicios = float(input("Digite a média das notas dos exercícios: "))

    # Calcula a média final usando a fórmula dada
    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

    # Determina o conceito com base na média final
    conceito = calcular_conceito(media_final)

    # Imprime os resultados
    print("Matrícula do aluno:", matricula)
    print("Média final:", "{:.2f}".format(media_final))
    print("Conceito:", conceito)

    # Determina se o aluno está aprovado ou reprovado
    if conceito in ['A', 'B', 'C']:
        print("Aprovado")
    else:
        print("Reprovado")

if __name__ == "__main__":
    main()
