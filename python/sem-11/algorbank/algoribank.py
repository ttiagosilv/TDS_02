def safe_data(processos, disponivel, max_need, alocados):
    
    num_processos = len(processos)
    num_recursos = len(disponivel)
    work = disponivel[:]
    termino = [False] * num_processos
    sequencia_segura = []

    while len(sequencia_segura) < num_processos:
        found = False
        for i in range(num_processos):
            if not termino[i]:
                exec_possible = True
                for j in range(num_recursos):
                    if max_need[i][j] - alocados[i][j] > work[j]:
                        exec_possible = False
                        break
                if exec_possible:
                    for k in range(num_recursos):
                        work[k] += alocados[i][k]
                    sequencia_segura.append(processos[i])
                    termino[i] = True
                    found = True
                    break
        if not found:
            break

    if len(sequencia_segura) == num_processos:
        return True, sequencia_segura
    else:
        return False, []

def banker_algorithm(processos, disponivel, max_need, alocados, request, process_num):
    
    num_recursos = len(disponivel)
    
    for i in range(num_recursos):
        if request[i] > max_need[process_num][i]:
            return False, "Erro: A solicitação excede a necessidade máxima."

        if request[i] > disponivel[i]:
            return False, "Erro: Não há recursos suficientes disponíveis."

    for i in range(num_recursos):
        disponivel[i] -= request[i]
        alocados[process_num][i] += request[i]

    is_safe, sequencia_segura = safe_data(processos, disponivel, max_need, alocados)
    
    if not is_safe:
        for i in range(num_recursos):
            disponivel[i] += request[i]
            alocados[process_num][i] -= request[i]
        return False, "Estado inseguro: A solicitação foi negada."
    return True, f"Solicitação concedida. Sequência segura: {sequencia_segura}"

# Exemplo de entrada
processos = [0, 1, 2, 3, 4]
disponivel = [3, 3, 2]  # Recursos disponíveis
max_need = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
alocados = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Solicitação de exemplo
request = [1, 0, 2]
process_num = 1

# Executa o Algoritmo
result, message = banker_algorithm(processos, disponivel, max_need, alocados, request, process_num)

print(message)

