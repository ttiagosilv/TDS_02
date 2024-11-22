def print_matrix(matrix, name):

    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(map(str, row)))

def is_safe_state(processes, available, max_need, allocated):
    num_processes = len(processes)
    num_resources = len(available)
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i]:
                exec_possible = True
                for j in range(num_resources):
                    if max_need[i][j] - allocated[i][j] > work[j]:
                        exec_possible = False
                        break
                if exec_possible:
                    for k in range(num_resources):
                        work[k] += allocated[i][k]
                    safe_sequence.append(processes[i])
                    finish[i] = True
                    found = True
                    break
        if not found:
            break

    if len(safe_sequence) == num_processes:
        return True, safe_sequence
    else:
        return False, []

def banker_algorithm(processes, available, max_need, allocated, request, process_num):
    num_resources = len(available)
    for i in range(num_resources):
        if request[i] > max_need[process_num][i]:
            return False, "Erro: A solicitação excede a necessidade máxima."

        if request[i] > available[i]:
            return False, "Erro: Não há recursos suficientes disponíveis."

    for i in range(num_resources):
        available[i] -= request[i]
        allocated[process_num][i] += request[i]
    is_safe, safe_sequence = is_safe_state(processes, available, max_need, allocated)
    
    if not is_safe:

        for i in range(num_resources):
            available[i] += request[i]
            allocated[process_num][i] -= request[i]
        return False, "Estado inseguro: A solicitação foi negada."

    return True, f"Solicitação concedida. Sequência segura: {safe_sequence}"

def read_list(size, name):

    lst = list(map(int, input(f"\nDigite a lista de {name} ({size} valores, separados por espaço): ").strip().split()))
    if len(lst) != size:
        raise ValueError(f"A lista deve ter exatamente {size} valores.")
    
    print(f"\nLista de {name}:")
    print(" ".join(map(str, lst)))
    
    return lst

def main():
    num_processes = 5
    num_resources = 3

    processes = list(range(num_processes))
    
    # Dados fixos para o exemplo
    available = [3, 3, 2]
    max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    allocated = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    print("Dados do sistema:")
    print(f"\nRecursos disponíveis:")
    print(" ".join(map(str, available)))
    
    print("\nNecessidade máxima:")
    print_matrix(max_need, "Necessidade Máxima")
    
    print("\nRecursos alocados:")
    print_matrix(allocated, "Recursos Alocados")

    print("\nDigite a solicitação de recursos:")
    request = list(map(int, input(f"Digite {num_resources} valores (separados por espaço): ").strip().split()))
    process_num = int(input("Digite o número do processo que faz a solicitação: "))

    if process_num < 0 or process_num >= num_processes:
        print("Número de processo inválido.")
        return

    result, message = banker_algorithm(processes, available, max_need, allocated, request, process_num)

    print(message)

if __name__ == "__main__":
    main()
