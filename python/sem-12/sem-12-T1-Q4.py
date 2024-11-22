def calcular_numero_da_sorte(data_nascimento):
    data_nascimento_str = str(data_nascimento)
    soma_digitos = 0 
    for digito in data_nascimento_str:
        soma_digitos += int(digito) 
    return soma_digitos

data_nascimento = int(input("Digite a sua data de nascimento no formato ddmmaaaa (8 dígitos): "))
numero_da_sorte = calcular_numero_da_sorte(data_nascimento)
print(f"O número da sorte é {numero_da_sorte}.")
