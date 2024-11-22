def main():
    idades = []  
    soma_idades = 0  

    while True:
        try:
            idade = int(input("Digite a idade (0 para encerrar): "))
            
            if idade == 0:
                break
            
            if idade > 0:
                idades.append(idade)
                soma_idades += idade  
            else:
                print("Idade inválida. Digite um valor positivo.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if idades:
        numero_pessoas = len(idades)
        idade_media = soma_idades / numero_pessoas
        menor_idade = min(idades)
        maior_idade = max(idades)
        
        print(f"Número de pessoas: {numero_pessoas}")
        print(f"Idade média: {idade_media:.2f}")
        print(f"Menor idade: {menor_idade}")
        print(f"Maior idade: {maior_idade}")
    else:
        print("Nenhuma idade válida foi digitada.")

if __name__ == "__main__":
    main()
