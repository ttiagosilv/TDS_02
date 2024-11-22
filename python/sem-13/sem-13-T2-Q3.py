def ler_notas(num_alunos):
    notas = [] 
    while len(notas) < num_alunos:
        try:
            nota = float(input(f"Digite a nota do aluno {len(notas) + 1}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número real.")
    
    return notas

def obter_indices_notas_suficientes(notas, limite):
    return [i for i, nota in enumerate(notas) if nota >= limite]

def exibir_indices(indices):
    print("Índices dos alunos com nota maior ou igual a 6:", indices)

def main():
    num_alunos = 50
    limite_nota = 6
    
    notas = ler_notas(num_alunos)
    indices_suficientes = obter_indices_notas_suficientes(notas, limite_nota)
    exibir_indices(indices_suficientes)

if __name__ == "__main__":
    main()
