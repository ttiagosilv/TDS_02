def ler_alunos(tamanho):
    alunos = []
    for i in range(tamanho):
        nome = input()
        while True:
            try:
                idade = int(input())
                altura = float(input())
                break
            except ValueError:
                print("Por favor, digite uma idade válida (número inteiro) e uma altura válida (número decimal).")
        alunos.append((nome, idade, altura))
    return alunos

def calcular_media_altura(alunos):
    total_altura = sum(aluno[2] for aluno in alunos)
    media = total_altura / len(alunos)
    return media

def alunos_acima_idade_e_abaixo_media(alunos, idade_minima, media_altura):
    """
    Retorna uma lista de alunos com mais de idade_minima anos e altura abaixo da média.
    """
    resultado = [aluno for aluno in alunos if aluno[1] > idade_minima and aluno[2] < media_altura]
    return resultado

def main():
    tamanho = 30
    idade_minima = 13
    alunos = ler_alunos(tamanho)
    media_altura = calcular_media_altura(alunos)
    alunos_filtrados = alunos_acima_idade_e_abaixo_media(alunos, idade_minima, media_altura)

    print(f"MAIORES DE {idade_minima} ANOS COM ALTURA ABAIXO DA MÉDIA")
    for nome, idade, altura in alunos_filtrados:
        print(nome)

if __name__ == "__main__":
    main()

